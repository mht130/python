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


#Running server
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
    # player_name=conn.recv(64).decode(FORMAT)
    # print(colored(f"{addr} connected as {player_name}","green"))
    global i
    global n

    while True:
        msg=conn.recv(64).decode(FORMAT)
        turn=i%2
        turn+=1
        # try:
        if msg!=disconnect_msg:
            if is_valid(msg):
                if turn==player_number:
                    i+=1                    #Change turn
                    n=n.replace(msg,players_char[player_number])
                    print(n)
                    conn.send(n.encode(FORMAT))
                    # conn2.send(n.encode(FORMAT))

                else:
                    conn.send("Err : NOT your turn, pls wait...".encode(FORMAT))
            else:
                conn.send("Err : NOT valid".encode(FORMAT))
        else:
            print(colored(f"{addr} Disconnected",'red'))
            try: 
                conn2.send(disconnect_msg.encode(FORMAT))
            except:
                pass                  
            break

        # except:
        #     break



try:
    conn1,addr1=s.accept()
    print(f"{addr1} connected")
    conn1.send("Waiting for 2nd player your number is 1".encode(FORMAT))
    conn2,addr2=s.accept()
    print(f"{addr2} connected")
    conn2.send(f"You are connected your number is 2".encode(FORMAT))
    conn1.send("Number 2 connected".encode(FORMAT))
    thread1=threading.Thread(target=handle_user,args=(conn1,addr1,1,conn2))
    thread2=threading.Thread(target=handle_user,args=(conn2,addr2,2,conn1))
    thread1.start()
    thread2.start()
except:
    s.close()