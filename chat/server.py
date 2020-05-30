import socket
import threading
from termcolor import colored
import sys
from time import sleep


port=5050
server_addr="0.0.0.0"
# server_addr=socket.gethostbyname(socket.gethostname())
FORMAT="utf-8"
header=64
disconnect_msg="!disconnect"
split_pattern="!://~"
clients=[]
clients_addr=[]
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((server_addr,port))

verbose=False
if len(sys.argv)>1 and sys.argv[1]=="--verbose":
	verbose=True
password=input("Enter client password (empty for no pass) : ")
print("[*] Server is Starting...")
print("[*] server is Running in " + server_addr,port)

def client_control(conn,addr):
	print(colored(f"[*] {addr} connected","green"),end="    ")
	try:
		send_to_client(str(addr[0])+" Connected",sender=conn,sender_addr=("Server","Server"))
	except:
		pass
	while stop_thread==False:
		msg_len=conn.recv(header).decode(FORMAT)          #Block 
		if msg_len:
			msg_len=int(msg_len)
			msg=conn.recv(msg_len).decode(FORMAT)         #Block

			if msg==disconnect_msg:            			  #disconnet client
				break
			if verbose:
				print("[+] "+colored(addr,"red"),end="")
				print(" : "+colored(msg,"green"))
			send_to_client(msg,sender=conn,sender_addr=addr)
	try:
		global clients
		clients.remove(conn)
	except ValueError:
		pass
	try:
		conn.shutdown(socket.SHUT_RDWR)
		conn.close()
	except:
		pass	
	print(f"[*] {addr} disconnected ",end="    ")
	print(f"Active connections : {threading.activeCount()-2}")
	if threading.activeCount()>1:
		try:
			send_to_client(str(addr[0])+" Disconnected",sender=conn,sender_addr=("Server","Server"))
		except:
			pass
stop_thread=False

def main():
	server.listen()
	while True:
		try:
			conn,addr=server.accept()
			pass_len=conn.recv(header).decode(FORMAT)
			passwd=conn.recv(int(pass_len)).decode(FORMAT)
			if password==passwd:
				clients.append(conn)
				clients_addr.append(addr)
				thread=threading.Thread(target=client_control,args=(conn,addr))
				thread.start()
				print(f"Active connections : {threading.activeCount()-1}")		
			else:
				send_to_client("password is wrong",sender="Server",sender_addr=("Server","Server"),conn=conn)
				send_to_client(disconnect_msg,sender="Server",sender_addr=("Server","Server"),conn=conn)
				print(colored(f"[*] {addr} tried to connect with wrong password","red"))
				conn.close()

		except KeyboardInterrupt:
			a=input("\nexit?(y/N)")
			choices=['y','Y','n','N']
			if a not in choices:
				a="n"
			if a=="y" or a=="Y":
				try:
					send_to_client(disconnect_msg,sender="Server",sender_addr=("Server","Server"))
					print(colored("\nShuting down","red"))
					sleep(3)

				except:
					pass
				global stop_thread
				stop_thread=True
				server.shutdown(socket.SHUT_RDWR)
				server.close()
				# sys.exit()
				break

def send_to_client(msg:str,sender=None,sender_addr=None,conn=None):       #conn=reciver
	if conn:
		msg=str(sender_addr[0])+split_pattern+msg
		message=msg.encode(FORMAT)
		msg_len=len(message)
		msg_len_encode=str(msg_len).encode(FORMAT)
		msg_len_encode+=b" "*(header-len(msg_len_encode))
		conn.send(msg_len_encode)
		conn.send(message)
	else:											#send to all
		receiver=clients
		for i in receiver:
			if i != sender:
				msg=str(sender_addr[0])+split_pattern+msg
				message=msg.encode(FORMAT)
				msg_len=len(message)
				msg_len_encode=str(msg_len).encode(FORMAT)
				msg_len_encode+=b" "*(header-len(msg_len_encode))
				i.send(msg_len_encode)
				i.send(message)

main()
