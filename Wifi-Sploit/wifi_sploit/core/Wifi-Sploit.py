#!/usr/bin/env python3

import typer
from typing import Optional
from rich.console import Console

from wifi_sploit.core.privileges import enforce_root
from wifi_sploit.core.deps import check_dependencies
from wifi_sploit.core.interface import get_interfaces, toggle_monitor
from wifi_sploit.modules.scanner import scan_networks
from wifi_sploit.modules.capture import capture_pmkid
from wifi_sploit.modules.convert import convert_to_hc22000
from wifi_sploit.ui.display import show_banner
from wifi_sploit.ui.prompts import select_interface, select_access_point

app = typer.Typer(help="Wifi-Sploit: Hybrid Wi-Fi Auditing Framework")
console = Console()

@app.command()
def main(
    iface: Optional[str] = typer.Option(None, "--iface", "-i", help="Wireless interface (e.g., wlan0)"),
    target: Optional[str] = typer.Option(None, "--target", "-t", help="Target BSSID (MAC address)"),
    channel: Optional[int] = typer.Option(None, "--channel", "-c", help="Channel number"),
    scan: bool = typer.Option(False, "--scan", help="Run scanner only and exit"),
):
    """
    Run interactively by default, or use flags for CI/automation.
    """
    enforce_root()
    check_dependencies()
    show_banner()

    if not iface:
        # Interactive fallback
        interfaces = get_interfaces()
        selected_iface = select_interface(interfaces)
        iface = selected_iface.name
        if not selected_iface.is_monitor:
            console.print(f"[yellow]Enabling monitor mode on {iface}...[/]")
            toggle_monitor(iface, True)
    else:
        console.print(f"[green]Using interface: {iface}[/]")

    if scan:
        console.print(f"[cyan]Scanning on {iface}...[/]")
        aps = scan_networks(iface)
        from wifi_sploit.ui.display import show_access_points
        show_access_points(aps)
        return

    if not target:
        console.print(f"[cyan]Scanning on {iface}...[/]")
        aps = scan_networks(iface)
        ap = select_access_point(aps)
        target = ap.bssid
        channel = ap.channel
    else:
        if channel is None:
            console.print("[bold red]Must provide --channel when specifying --target.[/]")
            raise typer.Exit(1)

    console.print(f"\n[bold green]Targeting {target} on channel {channel}[/]")
    pcap = capture_pmkid(iface, target, channel)
    
    if pcap:
        hc_file = convert_to_hc22000(pcap)
        if hc_file:
            console.print(f"\n[bold green]Success![/] Hash saved to: [cyan]{hc_file}[/]")
            console.print(f"Run: [yellow]hashcat -m 22000 {hc_file} wordlist.txt[/]")
    else:
        console.print("[bold red]Capture failed or no PMKID obtained.[/]")

    # Cleanup monitor mode on exit if we enabled it
    if not iface and get_interfaces():
        toggle_monitor(iface, False)

if __name__ == "__main__":
    app()