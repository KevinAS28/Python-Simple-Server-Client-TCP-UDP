import socket
from threading import Thread
import sys

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = ""
port = int(sys.argv[1])
udp.bind((ip, port))
#udp.listen()

def client_handler(data, info):
 udp1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 print("Connection from: %s:%d" %(info[0], info[1]))
 #terima = client_socket.recv(1024)
 print(data)
 print(info)
 udp1.sendto(b"oke", info)
finish = False
while not finish:
 try:
  data, addr = udp.recvfrom(1024)
  Thread(target=client_handler, args=[data, addr]).start()
 except KeyboardInterrupt:
  finish = True
  print("stop")
 	
