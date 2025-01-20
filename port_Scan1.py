#!/usr/bin/python3

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(2)
host = input("{*}Enter the host to scan: ")
port = int(input("{*} Enter the port no. : "))

def port_scan(port):
	if sock.connect_ex((host,port)):
		print(f"Port is closed  {port}")
	else:
		print(f"Port is opened{port}")

port_scan(port)

