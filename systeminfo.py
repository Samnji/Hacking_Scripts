# Runs the systeminfo command in windows and saves the information to a text file

import subprocess

cmd = "systeminfo"
subproc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
#returncall = subproc.wait()
#print(f'The return call of this command is {returncall}')
output, error = subproc.communicate()

if output:
	with open('systeminfo.txt', 'w') as file:
		file.write(output)
	#print(f'The OUTPUT:\n {output}')
elif error:
	with open('systeminfo.txt', 'w') as file:
		file.write(error)
	#print(f'The Returnd ERROR:\n {error}')
