import socket

ip = "127.0.0.1"
port = 2222
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.sendto("oke".encode("utf-8"), ((ip, port)))
print(udp.recvfrom(1024))
