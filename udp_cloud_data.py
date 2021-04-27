import socket
import json

UDP_IP = "52.152.229.29"
UDP_PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', UDP_PORT))

while True:
	data = s.recvfrom(1024)
	print("data: %s" % data)
