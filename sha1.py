#!/usr/bin/python

from urllib.request import urlopen
import hashlib
from termcolor import colored


sha1_hash = input("[*] Enter SHa1 Hash Value: ").strip()


passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read().decode('utf-8','ignore'))

lines = passlist.splitlines()
print(f"Checking {len(lines)} potential passwords. \n")

for password in lines:
	password = password.strip()
	hashguess = hashlib.sha1(password.strip().encode('utf-8')).hexdigest()
	print(colored(f"Trying password:'{password}' -> Hash: {hashguess}",'blue'))
	if hashguess == sha1_hash:
		print(colored("[+] The password is: " + str(password),'green'))
		quit()
	else:
		print(colored("[-] Password guess " + str(password) + " does not match, trying next ..",'red'))
print("Password not in passwordlist")
