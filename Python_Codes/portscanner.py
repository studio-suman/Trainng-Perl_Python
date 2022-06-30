
import sys
import socket
from typing import cast
import termcolor


def scan(target, ports):
	print(termcolor.colored('\n' + ' Starting Scan For ' + str(target),'green'))
	for port in range(1,ports):
		scan_port(target,port)


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		#sock.settimeout(1000) #Time Out
		sock.connect((ipaddress, port))
		print("[+] Port Opened " + str(port))
		sock.close()
	except socket.error as msg:
		print("\nCouldn't get response from socket: ", msg)
		sys.exit(1)
	else: 
		pass
	


targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)
