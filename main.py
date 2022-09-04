#!/usr/bin/python
#	Mau Copas? Belajar dulu ya dek wkwkwk
#	By XI RPL Smegrida

#port scanner

from queue import Queue
import socket
import threading
import time
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

print(bcolors.HEADER + """

██████╗░░█████╗░██████╗░████████╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
██████╔╝██║░░██║██████╔╝░░░██║░░░
██╔═══╝░██║░░██║██╔══██╗░░░██║░░░
██║░░░░░╚█████╔╝██║░░██║░░░██║░░░
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░

░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝ v.0.1
BY: XI-RPL SMEGRIDA
""")

target = input(bcolors.BOLD + bcolors.OKBLUE + "Masukan IP Address> " + bcolors.ENDC)
queue = Queue()
open_ports = []

def portscan(port):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((target, port))
		return True
	except:
		return False

def get_ports(mode):
	if mode == 1:
		for port in range(1, 1024):
			queue.put(port)
	elif mode == 2:
		for port in range(1, 49152):
			queue.put(port)
	elif mode == 3:
		ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
		for port in ports:
			queue.put(port)
	elif mode == 4:
		ports = input("Masukan port anda> ")
		ports = ports.split()
		ports = list(map(int, ports))
		for port in ports:
			queue.put(port)

def worker():
	while not queue.empty():
		port = queue.get()
		if portscan(port):
			print(bcolors.OKGREEN + "Port {} terbuka".format(port) + bcolors.ENDC)
			time.sleep(1)
			open_ports.append(port)
		else:
			print(bcolors.FAIL + "Port {} tertutup".format(port) + bcolors.ENDC)

def run_scanner(threads, mode):
	
	get_ports(mode)

	threads_list = []

	for t in range(threads):
		thread = threading.Thread(target=worker)
		threads_list.append(thread)

	for thread in threads_list:
		thread.start()

	for thread in threads_list:
		thread.join()

	print(bcolors.OKGREEN + "Port yang terbuka adalah: ", open_ports, bcolors.ENDC)


run_scanner(100,1)