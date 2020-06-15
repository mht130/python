import socket
from termcolor import colored
import sys
import threading
import os

if len(sys.argv)<2:
    print("usage : python server.py portno")
    sys.exit()

#Primary definitaions
ip='0.0.0.0'
port=int(sys.argv[1])
FORMAT="utf-8"
disconnect_msg="#!disconnect"
n='0123456789'
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
i=2
players_char=['','#','@']


#Run server
s.bind((ip,port))
s.listen(2)
print(colored(f"Server is running on {ip} and port {str(port)}","green"))


#input validation
def is_valid(msg):
    if msg:
        if msg.isnumeric():
            if 1<=int(msg)<=9:
                if n[int(msg)]==msg:
                    return True    
    return False


#handle each player
def handle_user(conn,addr,player_number,conn2):
    global i
    global n
    while True:
        try:
            msg=conn.recv(64).decode(FORMAT)
            turn=i%2
            turn+=1
            # try:
            if msg!=disconnect_msg:
                if is_valid(msg):
                    if turn==player_number:
                        i+=1                    #Change turn
                        n=n.replace(msg,players_char[player_number])
                        if not check_if_over(n):
                            conn.send(n.encode(FORMAT))
                            conn2.send(n.encode(FORMAT))
                        else:
                            msg=f"Game is over Player number {turn}({players_char[turn]}) win"
                            conn.send(msg.encode(FORMAT))
                            conn2.send(msg.encode(FORMAT))    
                            print(f"Game is over {turn} won")
                            conn2.send(disconnect_msg.encode(FORMAT))
                            conn.send(disconnect_msg.encode(FORMAT))
                            s.close()
                            break
                
                    else:
                        conn.send("Err : NOT your turn, pls wait...".encode(FORMAT))
                else:
                    conn.send("Err : NOT valid".encode(FORMAT))
            else:
                print(colored(f"{addr} Disconnected",'red'))
                conn.send("Disconected".encode(FORMAT))
                try: 
                    conn2.send(disconnect_msg.encode(FORMAT))
                except:
                    pass                  
                break
        except:
            break


#check if game is over
def check_if_over(n):
    if n[1]==n[2] and n[2]==n[3]:
        return True
    elif n[4]==n[5] and n[5]==n[6]:
        return True
    elif n[7]==n[8] and n[8]==n[9]:
        return True
    elif n[1]==n[4] and n[4]==n[7]:
        return True
    elif n[2]==n[5] and n[5]==n[8]:
        return True
    elif n[3]==n[6] and n[6]==n[9]:
        return True
    elif n[1]==n[5] and n[5]==n[9]:
        return True
    elif n[3]==n[5] and n[5]==n[7]:
        return True
    else:
        return False


#accept 2 player
try:
    conn1,addr1=s.accept()
    print(f"{addr1} connected")
    conn1.send("Waiting for 2nd player your number is 1 and you are #".encode(FORMAT))
    conn2,addr2=s.accept()
    print(f"{addr2} connected")
    conn2.send(f"You are connected your number is 2 and you are @".encode(FORMAT))
    conn1.send("Number 2 connected".encode(FORMAT))
    thread1=threading.Thread(target=handle_user,args=(conn1,addr1,1,conn2))
    thread2=threading.Thread(target=handle_user,args=(conn2,addr2,2,conn1))
    thread1.start()
    thread2.start()
except:
    s.close()