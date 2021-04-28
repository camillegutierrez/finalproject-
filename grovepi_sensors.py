""" EE 250L Lab 02: GrovePi Sensors """

"""python3 interpreters in Ubuntu (and other linux distros) will look in a
default set of directories for modules when a program tries to `import` one.
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages
The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import *
from grovepi import *

"""This if-statement checks if you are running this python file directly. That
is, if you run `python3 grovepi_sensors.py` in terminSal, this if-statement will
be true"""
if __name__ == '__main__':

    light_sensor = 0 # Connect the Grove Light Sensor to analog port A0
    sound_sensor = 1 # Connect the Grove Sound Sensor to analog port A1

    grovepi.pinMode(light_sensor,"INPUT")
    grovepi.pinMode(sound_sensor, "INPUT")
    time.sleep(1)

    import socket,json
    import numpy as np
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    while True:

        try:
            now = time.time()
            sound_values = []
            while (time.time() - now) < 0.5:
                # Read sensor value from sound_sensor
                sound_values += [grovepi.analogRead(sound_sensor)]
            sound_std = np.std(sound_values)
            # Read sensor value from light_sensor
            light_value = grovepi.analogRead(light_sensor)
            #print(light_value)

            data = {"sound":sound_std, "light": light_value}
            datastring = json.dumps(data)
            print(datastring)
            # ADD: Send light and sound data to the cloud
            s.sendto(datastring.encode(), ("52.152.229.29", 8080))

            intruder, addr = s.recvfrom(1024)
            print("Intruder?: %s" % intruder)

        except Exception as e:
            print (e)
