import subprocess as s
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface",  help="Enables you to enter the interface you want to change the mac address.")
parser.add_option("-m", "--mac", dest="new_mac", help="Here is where you enter the new mac address.")

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


