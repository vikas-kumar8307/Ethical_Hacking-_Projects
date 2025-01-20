#!usr/bin/python
'''
import hashlib

hashvalue= input("Enter a string to hash:")
hashobj = hashlib.md5()
hashobj.update(hashvalue.encode())
 
print(hashobj.hexdigest())

hashobj2 = hashlib.sha1()
print(hashobj2.hexdigest())

hashobj3 = hashlib.sha256()
print(hashobj3.hexdigest())

hashobj4 = hashlib.sha512()
print(hashobj4.hexdigest())'''

              
#!/usr/bin/python

import hashlib

# Get user input
hashvalue = input("Enter a string to hash: ")

# MD5 hash
hashobj = hashlib.md5()
hashobj.update(hashvalue.encode())
print("MD5:", hashobj.hexdigest())

# SHA-1 hash
hashobj2 = hashlib.sha1()
hashobj2.update(hashvalue.encode())
print("SHA-1:", hashobj2.hexdigest())

# SHA-256 hash
hashobj3 = hashlib.sha256()
hashobj3.update(hashvalue.encode())
print("SHA-256:", hashobj3.hexdigest())

# SHA-512 hash
hashobj4 = hashlib.sha512()
hashobj4.update(hashvalue.encode())
print("SHA-512:", hashobj4.hexdigest())
