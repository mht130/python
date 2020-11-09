import socket
import sys
from termcolor import colored
import os
import threading

#user switch check
if len(sys.argv)<2:
    print("usage : python client.py portno")
    sys.exit()

#Primary definitaions
FORMAT="utf-8"
#ip='192.168.43.164'
ip='192.168.1.104'
port=int(sys.argv[1])
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
def board(n,ch):
    os.system("clear")
    print(f"       |     |     ")
    print(f"    {n[1]}  |  {n[2]}  |  {n[3]}  ")
    print(f"  _________________")
    print(f"       |     |     ")
    print(f"    {n[4]}  |  {n[5]}  |  {n[6]}  ")
    print(f"  _________________")
    print(f"    {n[7]}  |  {n[8]}  |  {n[9]}   ")
    print(f"       |     |      ")
    print(f"                             You are {ch}      ")
    print()

board(n,'-')


def reciver(ch):
    global running
    while running:
        try:
            res=s.recv(64).decode(FORMAT)
            if res==disconnect_msg:
                break
            elif res[:3]=="Err":
                print(res)
            elif res[0:12]=='Game is over':
                print(res)
                running=False
                break
            else:
                board(res,ch)
        except:
            pass




# connected msg
msg=s.recv(64).decode(FORMAT)
ch=msg[::-1][0]
print(msg)
if msg=='Waiting for 2nd player your number is 1 and you are #':
    #number 2 connected
    msg=s.recv(64).decode(FORMAT)
    print(msg)



thread=threading.Thread(target=reciver,args=(ch))
thread.start()
#main loop
while running:
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
