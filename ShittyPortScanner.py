import sys
import socket
from datetime import datetime

if len(sys.argv) == 2: # Counts the number of system arguments parsed in, while the you run the program
	target = socket.gethostbyname(sys.argv[1]) # Changes hostname to IPV4
	
else:
	print('-' * 50)
	print("Invalid number of arguments.")
	print("Syntax: python ShittyPortScanner <ip> or hostname")
	print('-' * 50)
	sys.exit()

# Pretty Banner
print('-' * 50)
print("Scanning {}".format(target))
start = int(input("Enter the starting port: "))
end = int(input("Enter the ending port: "))

print("Time started: " + str(datetime.now()))

try:
	for port in range(start, 80+1):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.05) #time in seconds and its a float
		result = s.connect_ex((target, port))
		print("Checking port {}".format(port))
		if result == 0:
			print("Port {} open".format(port))

		s.close()

	print("Time finished: " + str(datetime.now()))
except KeyboardInterrupt:
	print("Exiting program...")
else:
	pass
finally:
	print('-' * 50)