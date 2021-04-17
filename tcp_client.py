"""
Server IP is 52.152.229.29, ports are 5000-5008, socket is UNIX TCP
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
"""

import socket

def main():

    # TODO: Create a socket and connect it to the server at the designated IP and port
    HOST = '52.152.229.29'
    PORT = 8080

    # TODO: Get user input and send it to the server using your TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    	s.connect((HOST, PORT))
    	user_input = input("Enter a message: ")
    	s.sendall(user_input.encode())
    	data = s.recv(256)

    # TODO: Receive a response from the server and close the TCP connection
    	print(data.decode('utf-8'))
    	s.close()

if __name__ == '__main__':
    main()
