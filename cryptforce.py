#!usr/bin/python
import crypt
from termcolor import colored

def crackpass(cryptword):
	salt = cryptword[0:2]
	dict = open("dict.txt",'r')
	for word in dict.readlines():
		word = word.strip('\n')
		cryptpass = crypt.crypt(word, salt)
		if (cryptword == cryptpass):
			print(colored("[+] Found Password:" + word,'green'))
			return
	
	

def main():
	passfile = open('pass.txt','r')
	for line in passfile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptword = line.split(':')[1].strip(' ').strip('\n')
			print(colored("[+] Cracking Password For :" + user,'blue'))
			crackpass(cryptword)
			print(colored("[-] Print Password not found",'red'))

main()
