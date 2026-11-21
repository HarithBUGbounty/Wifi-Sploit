### Command-Line Mode

For automation or targeted attacks, you can bypass the interactive menus entirely. 

```text
Usage: Wifi-Sploit.py [OPTIONS]

Options:
  -i, --iface TEXT      Wireless interface (e.g., wlan0)
  -t, --target TEXT     Target BSSID (MAC address, e.g., AA:BB:CC:DD:EE:FF)
  -c, --channel INTEGER Target channel number (Required if --target is used)
  --scan                Run scanner only and exit
  --help                Show this message and exit

Examples:
  # Interactive Mode (Prompts for everything)
  $ sudo python3 Wifi-Sploit.py

  # Scan Only (List APs and exit)
  $ sudo python3 Wifi-Sploit.py --scan

  # Targeted Capture (Skip menus, capture PMKID directly)
  $ sudo python3 Wifi-Sploit.py -i wlan0 -t AA:BB:CC:DD:EE:FF -c 6
