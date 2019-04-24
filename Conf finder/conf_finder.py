import os,sys
from termcolor import colored

help_text='''usage : python conf_finder [program name]
use --all for all conf files'''
counter=1
if(len(sys.argv)<2 or sys.argv[1]=='' or sys.argv[1]=='-h' or sys.argv[1]=='--help'):
	print(colored(help_text,'green'))
else:
	file_name=sys.argv[1]
	try:
		for root,dirs,files in os.walk('/'):
			for file in files:
				if(file.endswith('.conf') or file.endswith('.cfg')):
					if(file.find(file_name)==0):
						print(colored(str(counter)+') '+root+'/'+str(file),'green'))
						counter+=1
					elif(file_name=='--all'):
						print(colored(str(counter)+') '+root+'/'+str(file),'green'))
						counter+=1
	except Exception:
		print(colored("Something goes wrong",'red'))
