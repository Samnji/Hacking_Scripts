with open("command prompt commands.txt", 'r') as file:
	list_file = file.readlines()

	for line in list_file:
		print(line)