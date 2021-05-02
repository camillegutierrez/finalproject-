""" EE 250L Final Project: Rpi-Client Side """

# import libraries
import sys
import time
import grovepi
from grove_rgb_lcd import *
from grovepi import *
import socket,json
import numpy as np
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')


if __name__ == '__main__':

    light_sensor = 0 # Connect the Grove Light Sensor to analog port A0
    sound_sensor = 1 # Connect the Grove Sound Sensor to analog port A1

    grovepi.pinMode(light_sensor,"INPUT")
    grovepi.pinMode(sound_sensor, "INPUT")
    time.sleep(1)

    # Server IP address and port #
    UDP_IP = "52.152.229.29"
    UDP_PORT = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP Connection


    while True:

        try:
            now = time.time()
            sound_values = []
            while (time.time() - now) < 0.5:
                # Read sensor value from sound_sensor for the first 0.5 seconds of 1 second
                sound_values += [grovepi.analogRead(sound_sensor)]
            sound_std = np.std(sound_values) # Take standard deviation of sound values
            # Read sensor value from light_sensor
            light_value = grovepi.analogRead(light_sensor)

            # Store data in json format and send to cloud
            data = {"sound":sound_std, "light": light_value}
            datastring = json.dumps(data)
            print(datastring)
            s.sendto(datastring.encode(), (UDP_IP, UDP_PORT))

            # Receive intruder information from the cloud
            intruder, addr = s.recvfrom(1024)
            intruder = intruder.decode()
            print("Intruder?: %s" % intruder)

            # Update LCD screen based on intruder information
            if intruder == "Intruder":
                setText_norefresh("Intruder, beware")
                setRGB(255,0,0)
            else:
                setText_norefresh("House is safe   ")
                setRGB(0,255,0)

        except Exception as e:
            print (e)
