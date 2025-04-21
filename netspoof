#!/usr/bin/env python3
import os
import subprocess
import argparse
from colorama import init, Fore, Back, Style
import random
import time

# initialize colorama
init()

parser = argparse.ArgumentParser(description="A program which can used to spoof/change mac address of devices on a network.")
parser.add_argument('-i', '--interface', help='wireless interface', required=True)
args = parser.parse_args()

mac_addresses = [
	"00:1B:44:11:3A:B7", "2A:6C:E5:88:99:01", "4C:AA:16:D9:63:12", "00:23:6C:11:56:98", "1A:2B:3C:4D:5E:6F",
	"02:00:00:00:00:00", "12:34:56:78:9A:BC", "98:76:54:32:10:FE", "5E:4D:3C:2B:1A:00", "DE:AD:BE:EF:12:34",
	"BA:DC:FE:09:87:65", "AA:BB:CC:DD:EE:FF", "90:8F:7E:6D:5C:4B", "B4:C5:D6:E7:F8:09", "0A:1B:2C:3D:4E:5F",
	"F0:E1:D2:C3:B4:A5"
]

interface = args.interface

if not 'SUDO_UID' in os.environ:
	print(f"{Fore.RED}Error: Requires admin Privilege{Style.RESET_ALL}")

else:
	# banner
	print(Fore.BLACK + Back.WHITE + f"***************( Net_Spoofer )****************" + Style.RESET_ALL)
	print(Fore.BLACK + Back.WHITE + f"   By Sys_br3ach3r                            " + Style.RESET_ALL)

	try:
		mac_addr = random.choice(mac_addresses)
		print(f" changing {Fore.BLUE + interface + Style.RESET_ALL} mac address to {Fore.GREEN + mac_addr + Style.RESET_ALL}\n")

		subprocess.run(['ifconfig', interface, 'down'])
		subprocess.run(['ifconfig', interface, 'hw', 'ether', mac_addr])
		subprocess.run(['ifconfig', interface, 'up'])
		subprocess.run(['ifconfig'])
		print(f"\n{Fore.BLACK + Back.WHITE}       Program Completed.                     " + Style.RESET_ALL)

	except KeyboardInterrupt:
		abort_countdown = [5, 4, 3, 2, 1]
		for count in abort_countdown:
			print(f"\r ({Fore.RED}Ctrl + c{Style.RESET_ALL}) Aborting in {count}", end="")
			time.sleep(0.5)
		quit()


