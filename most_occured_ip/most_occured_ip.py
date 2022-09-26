# This script checks the most occurred ip address in a log file
# The log file should be stored in the same directory or folder

import sys
import re
from datetime import datetime

class OccurredIp:
	def __init__(self):
		self.ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
		self.file_name = file_name

	# You first of all store the data or information in the log file in form of a list of words
	def wordList(self):
		final_word_list = []
		with open(self.file_name, 'r') as file:
			return file.read().split(" ")
	
	# Then count the occurrence of each ip storing the counts in a set of numbers
	def ipCount(self, word_list):
		word_count = []
		
		print(f"{datetime.now()}: Checking for ips!!")
		for word in word_list:
			if self.ip_add_pattern.search(word):
				word_count.append(word_list.count(word))

		print(f"{datetime.now()}: Done checking for ips!!\n\n")

		return set(word_count)

	# Then sort the set since it has unique numbers to get the greatest count
	# Then search for the ip with the same number of counts as the greatest count
	def mostOccurredIp(self, count_list, word_list):
		sorted_list = sorted(count_list)
		print(f"List of sorted ip counts:")
		print(sorted_list)
		most_word_count = sorted_list[len(sorted_list) - 1]
		print(f"{most_word_count} is the greatest ip count.\n\n")
		
		print(f"{datetime.now()}: Checking for the most occurred ip!!")
		for word in word_list:
			if self.ip_add_pattern.search(word) and word_list.count(word) == most_word_count:
				print(f"{datetime.now()}: Found the ip!!")
				return word
				break
		

if len(sys.argv) == 2:
	print((" "*25)+ "Most occurred Ip Determiner")
	print("-" * 100)

	file_name = sys.argv[1]
	O = OccurredIp()
	word_list = O.wordList()
	set_word_count = O.ipCount(word_list)

	most_occurred_ip = O.mostOccurredIp(set_word_count, word_list)
	print(f"{most_occurred_ip} is the most occurred ip")

	print("-" * 100)

else:
	print("-" * 100)
	print("Invalid Syntax!!")
	print("Syntax: python3 most_occurred_ip.py log_file.log")
	print("-" * 100)