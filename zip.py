import zipfile; from pyfiglet import *; from termcolor import * 
print(colored(figlet_format('ZipCracker'), 'yellow'))

filename = raw_input(colored('Enter target zip: ', 'blue'))
dictionary = raw_input(colored('Enter Wordlist: ', 'blue')) 

password = None 
try:
	file_to_open = zipfile.ZipFile(filename) 
except:
	print (colored('[-] ZipFile not found', 'red'))
	exit()
try:
	f = open(dictionary, 'r')
except:
	print (colored('[-] Wordlist not found', 'red'))
	exit()
for line in f.readlines(): 
	password = line.strip('\n') 
	try: 
		file_to_open.extractall(pwd=password)
		print (colored('[+] Password found == ' + password, 'green'))
	except:
		print (colored('[-] Cracking ' + filename + ' : ' + password, 'red')) 

