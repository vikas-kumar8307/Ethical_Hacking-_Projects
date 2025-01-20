#!/usr/bin/python

import socket

def retBanner(ip,port):
	try: 
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner
	except:
		return

def main():
	ip = raw_input("[+] Enter Target IP: ")
	for port in range(1, 100):
		Port = str(port)
		banner = retBanner(ip,port)
		if banner:
			print "[+]" + ip + ": Port=" + Port + " Banner:" + banner
main()
