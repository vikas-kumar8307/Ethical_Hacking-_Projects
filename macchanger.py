#!/usr/bin/python

import subprocess 

def change_mac_address(interface,mac):

	subprocess.call(["ip ","link","set",interface,"down"])
	subprocess.call(["ip ",interfce, "hw","ether",mac])
	subprocess.call(["ip ",interface,"up"])


def main():
	interface = str(input("[*] Enter interface to change MAC ADDR> :"))
	new_address = input("[+] ENter MAC ADDR> change to: ")

	before_change = subprocess.check_output(["ip",interface])
	change_mac_address(interface,new_address)
	after_change = subprocess.check_output(["ip" + interface]).decode("utf-8")

	if before_change == after_change:
		print("[-] Failed to change mac address")

	else:

		print("[+ Mac address change successfully to ]" + new_mac_address + "On Interface: "+ inferface)

if __name__=="__main__":
	main()
