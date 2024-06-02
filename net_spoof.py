#!/usr/bin/python

import subprocess
import os
import argparse

# arguments parsing
parser = argparse.ArgumentParser(description='IP addr & mac-changer ( Created by f3ar_0f_th3_unkn0wn)')
parser.add_argument('-i', '--interface', help='wireless interface', required=True)
parser.add_argument('-m', '--mac', help='fake mac address')
parser.add_argument('-ip', '--ipaddr', help='fake ip address')

args = parser.parse_args()

ip_addr = args.ipaddr
mac_addr = args.mac
interface = args.interface

if not 'SUDO_UID' in os.environ:
        print('Run as Root (sudo)')

else:
	subprocess.run(['ifconfig', interface, ip_addr])

	subprocess.run(['ifconfig', interface, 'down'])
	subprocess.run(['ifconfig', interface, 'hw', 'ether', mac_addr])
	subprocess.run(['ifconfig', interface, 'up'])
	subprocess.run(['ifconfig'])
