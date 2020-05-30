import socket
import threading
import sys
from termcolor import colored

# port=5050
# server_addr="192.168.1.103"
FORMAT="utf-8"
header=64
disconnect_msg="!disconnect"
split_pattern="!://~"

stop_thread=False
server_addr=input("Enter server ip : ")
port=input("Enter port number : ")
port=int(port)
password=input("Enter the password(empty for none) : ")
try:
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((server_addr,port))
    print(colored("Connected","green"))
except:
    print(colored("Connection Faild1","red"))


def send(msg):
    message=msg.encode(FORMAT)
    msg_len=len(message)
    msg_len_encode=str(msg_len).encode(FORMAT)            # encode msg len
    msg_len_encode+=b" "*(header-len(msg_len_encode))     # raise the msg_len size up to 64
    client.send(msg_len_encode)                           # send msg len
    client.send(message)                                  # send msg

def receive():
    try:
        while stop_thread==False:
            msg_len=client.recv(header).decode(FORMAT)
            if msg_len:
                msg_len=int(msg_len)
                msg=client.recv(msg_len).decode(FORMAT)
                msg=msg.split(split_pattern)
                if msg[0]=="Server" and msg[1]==disconnect_msg:
                    disconnect()
                    break
                # print("[-] "+colored(msg,"red"))
                print("[+] "+colored(msg[0],"red"),end="") #msg[0] is sender
                print(" : "+colored(msg[1],"green"))       #msg[1] is message
    except:
        print(colored("Connection Faild","red"))

def main():
    receiver_thread=threading.Thread(target=receive)
    receiver_thread.start()
    send(password)
    while True:
        try:
            msg=input()
            send(str(msg))
            if msg==disconnect_msg:
                raise KeyboardInterrupt
        except KeyboardInterrupt:
            disconnect()
            break


def disconnect():
        global stop_thread
        stop_thread=True
        try:
            send(disconnect_msg)
            client.shutdown(socket.SHUT_RDWR)
            client.close()
        except:
            pass
        print(colored("\ngoodbye","red"))
        sys.exit()


main()
