import time as t
import os

def progress_bar(time):
    a='[--------------------]'
    print(a)
    counter=1
    while(counter<=20):
        t.sleep(time)
        a=a.replace('-','#',1)
        os.system('clear')
        print(a+'  '+str((counter*5))+'%')
        counter+=1

if __name__=='__main__':
    progress_bar(0.5)
