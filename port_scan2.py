#!/usr/bin/python3

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(.1)

host = input("{*}Enter the host to scan: ")


def port_scan(port):
        if sock.connect_ex((host,port)):
		print(colored(f"[!!] Port is closed  {port}",'red')) 
        else:
                print(f"[+] Port is opened{port}")

for port in range(1,100):
	port_scan(port)


