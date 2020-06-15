import socket
import sys
from termcolor import colored
import os
import threading

#user switch check
if len(sys.argv)<3:
    print("usage : python client.py portno player_name")
    sys.exit()

#Primary definitaions
FORMAT="utf-8"
# ip='192.168.43.164'
ip='192.168.1.103'
port=int(sys.argv[1])
player_name=sys.argv[2]
disconnect_msg="#!disconnect"
n='0123456789'
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
running=True
# try to connect to server
try:
    s.connect((ip,port))
    print(colored("connected",'green'))
    # s.send(player_name.encode(FORMAT))
except:
    print(colored("Faild to connect",'red'))
    s.close()
    sys.exit()


#draw board
def board(n,turn=0):
    os.system("clear")
    print(f"       |     |     ")
    print(f"    {n[1]}  |  {n[2]}  |  {n[3]}  ")
    print(f"  _________________")
    print(f"       |     |     ")
    print(f"    {n[4]}  |  {n[5]}  |  {n[6]}  ")
    print(f"  _________________")
    print(f"    {n[7]}  |  {n[8]}  |  {n[9]}   ")
    print(f"       |     |      ")


board(n)


def reciver():
    while running:
        try:
            res=s.recv(64).decode(FORMAT)
            if res==disconnect_msg:
                break
            elif res[:3]=="Err":
                print(res)
            else:
                print("ok : "+res)
        except:
            pass




# connected msg
msg=s.recv(64).decode(FORMAT)
print(msg)
if msg=='Waiting for 2nd player your number is 1':
    #number 2 connected
    msg=s.recv(64).decode(FORMAT)
    print(msg)

thread=threading.Thread(target=reciver)
thread.start()
#main loop
while True:
    try:
        msg=input("")
        if msg.isnumeric():
            s.send(msg.encode(FORMAT))
            if msg==disconnect_msg:
                break
        else:
            print("Not valid")
    except:
        print(colored("\nDisconnected",'red'))
        running=False
        s.send(disconnect_msg.encode(FORMAT))
        s.close()
        break
