## ⚠️ Warning

**Do not use this on networks you do not own or do not have explicit, written permission to test.**

Capturing PMKIDs and EAPOL handshakes is illegal in most jurisdictions without authorization. This is a tool for lab environments and authorized penetration tests. The author assumes zero liability for misuse. If you point this at your neighbor's router, you're committing a crime. Get permission. Stay legal. And be good boyz&Girlz 

## Usage 🌵

Always run as root. Monitor mode and raw socket operations require it.

### Interactive Mode
Running the script without flags launches the interactive UI. It will guide you through selecting your adapter, putting it into monitor mode, scanning for targets, and executing the capture.

```bash
sudo python3 Wifi-Sploit.py

Usage: Wifi-Sploit.py [OPTIONS]

Options:
  -i, --iface TEXT      Wireless interface (e.g., wlan0)
  -t, --target TEXT     Target BSSID (MAC address, e.g., AA:BB:CC:DD:EE:FF)
  -c, --channel INTEGER Target channel number
  --scan                Run scanner only and exit
  --help                Show this message and exit

Examples:
  # Interactive Mode (Prompts for everything)
  $ sudo python3 Wifi-Sploit.py

  # Scan Only (List APs and exit)
  $ sudo python3 Wifi-Sploit.py --scan

  # Targeted Capture (Skip menus)
  $ sudo python3 Wifi-Sploit.py -i wlan0 -t AA:BB:CC:DD:EE:FF -c 6
```
## Quick Installation

Requires Linux (Kali, Parrot, Ubuntu, etc.), a wireless card that supports monitor mode, and Python 3.8+.

**1. Install system dependencies:**
```bash
sudo apt update
sudo apt install hcxdumptool hcxtools iw iproute2 python3-venv -y
```
```bash
git clone https://github.com/HarithBUGbounty/Wifi-Sploit.git
cd Wifi-Sploit
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```
## Run It As Root:
```bash
sudo python3 Wifi-Sploit.py
```
