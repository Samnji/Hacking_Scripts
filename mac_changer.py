# Check if argv are 2 with -h should run the program else output help banner
import sys
import subprocess as s
import optparse

def macChanger():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface",  help="Required --> Enables you to enter the interface you want to change the mac address.")
	parser.add_option("-m", "--mac", dest="new_mac", help="Required --> Here is where you enter the new mac address.")

	(option, argument) = parser.parse_args()
	interface = option.interface
	new_mac = option.new_mac

	subproc = s.Popen("ifconfig " + interface, shell=True, stdout=s.PIPE, stderr=s.PIPE, universal_newlines=True)
	(output, error) = subproc.communicate()

	print("[+] These are the initial " + interface + "'s info\n")
	print(output)

	print("[+] Changing interface " + interface + "'s mac address to " + new_mac + "\n")
	s.call(["sudo", "ifconfig", interface, "down"])
	s.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
	s.call(["sudo", "ifconfig", interface, "up"])

	subproc = s.Popen("ifconfig " + interface, shell=True, stdout=s.PIPE, stderr=s.PIPE, universal_newlines=True)
	(output, error) = subproc.communicate()

	print("[+] These are the final " + interface + "'s info\n")
	print(output)


print('-' * 50)
if len(sys.argv) == 2: # Counts the number of system arguments parsed in, while the you run the program
	macChanger()

elif len(sys.argv) ==3:
	macChanger()

else:
	# Help banner
	print("Invalid number of arguments.")
	print("Syntax: python mac_changer.py <-i> <-m>")
	print("Check help")
	print("Syntax: python mac_changer.py <-h> <-m>")
	
print('-' * 50)


