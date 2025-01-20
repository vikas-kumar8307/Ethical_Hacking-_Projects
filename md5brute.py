#!/usr/bin/python

from termcolor import colored
import hashlib

def tryOpen(wordlist):
	global pass_file
	try:
		pass_file = open(wordlist,"r")
	except:
		print("[-] No Such FIle At That Path!!")
		quit()




pass_hash = input("[+] Enter MD5 Hash Value:")
wordlist = input("[+] Enter path to the password File:")
tryOpen(wordlist)

for word in pass_file:
	print(colored("[+] Trying:" + word.strip("\n"),'red'))
	encodeW = word.encode('utf-8')
	md5_digest = hashlib.md5(encodeW.strip()).hexdigest()
	
	if md5_digest == pass_hash:
		print(colored("[+] Password Found::->" + word,'green'))
		exit()

print("{!} Password not in list")
