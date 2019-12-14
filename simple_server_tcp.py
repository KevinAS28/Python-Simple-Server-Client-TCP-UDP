import socket
from threading import Thread
import sys
ip = "0.0.0.0"
port = int(sys.argv[1])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((ip, port))
sock.listen()
checkpoint = 0
print("listening %s:%d ..."%(ip, port))
finish = False
def client_handler(client_socket, info):
 global checkpoint
 if finish:
  sys.exit(0)
 print("Connection from %s:%d" %(info[0], info[1]))
 print(client_socket.recv(2048))
 client_socket.send(b"DID IT\r\n")
 print("okay{x}".format(x=checkpoint))
 client_socket.close()
 checkpoint+=1

while True:
 try:
  client, addr = sock.accept()
  Thread(target=client_handler, args=(client, addr)).start()
 except KeyboardInterrupt as e:
  print("Stop\r\n")
  sock.close()
  sys.exit(0)
  
 
