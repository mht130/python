import sys,os
from termcolor import colored
help_text='''
Usege : python3 eyn.py [file(txt)] [key]
'''
def eyn(file_dir,key):
        file=open(file_dir,'r')
        eyn=str()
        if(file):
            for line in file:
                while(len(line)>len(key)):
                    key+=key
                c=0
                for i in line:
                    r=ord(i)+ord(key[c])
                    r=r+11
                    eyn+=chr(r)
                    c+=1
                eyn+='\n'
        return eyn

if(len(sys.argv)!=3 or sys.argv[1]=='-h'):
    print(colored(help_text,'green'))
elif(not os.path.isfile(sys.argv[1])):
    print(colored("{} file dose not exist".format(sys.argv[1]),'red'))
else:
    try:
        file_dir=sys.argv[1]
        key=sys.argv[2]
        eyn_txt=eyn(file_dir,key)
        eyn_file=open(file_dir[:-4:]+'_eyn.txt','w')
        eyn_file.write(eyn_txt)
        eyn_file.close
        print(colored('File saved successfully','green'))
    except:
        print(colored('Something goes wrong','red'))
