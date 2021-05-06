""" EE 250 Final Project: Azure-Server Side """

# import libraries
import socket
import json

# Cloud IP address and port
UDP_IP = "52.152.229.29"
UDP_PORT = 8080

# UDP Server Connection
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', UDP_PORT))

while True:
        #receive light and sound data from rpi
        data, addr = s.recvfrom(1024)
        data = data.decode()
        print("data: %s" % data)

        # get light and sound data from json
        light = json.loads(data)['light']
        sound = json.loads(data)['sound']
		output = b""


        """ Data processing: Compare light and sound data
         with darkness and loud noise thresholds. """
        if light < 100: #night
                if sound > 5: #loud
                        output = b"Intruder"
                else:
                        output = b"Safe"
        else:
                output = b"Safe"

        # Send intruder information back to rpi for visualization
        s.sendto(output, addr)
