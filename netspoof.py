import os
import subprocess
import argparse
from colorama import init, Fore, Back, Style

# initialize colorama
init()

parser = argparse.ArgumentParser(description="A program which can used to spoof/change mac address of devices on a network.")
parser.add_argument('-i', '--interface', help='wireless interface', required=True)
args = parser.parse_args()

mac_addresses = [
	"00:1B:44:11:3A:B7", "2A:6C:E5:88:99:01", "4C:AA:16:D9:63:12", "00:23:6C:11:56:98", "1A:2B:3C:4D:5E:6F",
	"FF:FF:FF:FF:FF:FF", "02:00:00:00:00:00", "12:34:56:78:9A:BC", "98:76:54:32:10:FE", "AB:CD:EF:01:23:45",
	"5E:4D:3C:2B:1A:00", "33:44:55:66:77:88", "DE:AD:BE:EF:12:34", "BA:DC:FE:09:87:65", "11:22:33:44:55:66",
	"AA:BB:CC:DD:EE:FF", "01:02:03:04:05:06", "0F:1E:2D:3C:4B:5A", "67:56:45:34:23:10", "78:9A:BC:DE:F0:12",
	"21:0F:E3:D5:CB:A9", "90:8F:7E:6D:5C:4B", "B4:C5:D6:E7:F8:09", "0A:1B:2C:3D:4E:5F", "C1:D2:E3:F4:05:16",
	"89:7A:6B:5C:4D:3E", "F0:E1:D2:C3:B4:A5", "45:36:27:18:09:FA", "23:45:67:89:AB:CD"
]

interface = args.interface

if not 'SUDO_UID' in os.environ:
	print(f"{Fore.RED}Error: Requires admin Privilege{Style.RESET_ALL}")

else:
	# banner
	print(Fore.BLACK + Back.WHITE + f"***************( Net_Spoofer )****************" + Style.RESET_ALL)
	print(Fore.BLACK + Back.WHITE + f"   By Sys_br3ach3r                            " + Style.RESET_ALL)

	for mac_addr in mac_addresses:
		subprocess.run(['ifconfig', interface, 'down'])
		subprocess.run(['ifconfig', interface, 'hw', 'ether', mac_addr])
		subprocess.run(['ifconfig', interface, 'up'])
		subprocess.run(['ifconfig'])
		print(f"\n{Fore.BLACK + Back.WHITE}       Program Completed.                     " + Style.RESET_ALL)

