import threading
from smbus2 import SMBusWrapper
import time
import sys
#from clean_print import Cprint
import math
import numpy as np
from read_magneto_data import readData as read_magnet


#length = 455 cm
#width = 149 cm

#data :: R, F, L, B
#        1, 2, 4, 3
d_format = {'fwd' : 1, 'bkwd' : 3, 'left' : 2, 'right' : 0}

address = 0x05
length = 455
width = 149
pos = {'x':0, 'y':0}
magnet_data = None
exitFlag = 0

class magReadThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        readMagneto(self.name)

def readMagneto(name):
    global magnet_data
    while True:
        if exitFlag:
            name.exit()

        magnet_data = read_magnet()
        time.sleep(0.01)

def readData():
    with SMBusWrapper(1) as bus:
        try:
            block = bus.read_i2c_block_data(address, 0, 8)
        except:
            print("I2C ERROR while reading")
            return None

        for b in block:
            if b & 0xFF == 0xFF:
                print('Read error 0xFF')
                return None
        data = []
        data.append(block[0] << 8 | block[1])
        data.append(block[2] << 8 | block[3])
        data.append(block[4] << 8 | block[5])
        data.append(block[6] << 8 | block[7])

    return data

#def calculate_position(data):



if __name__ == '__main__':
    thread1 = magReadThread(1, 'Thread-1')
    try:
        thread1.start();
    except KeyboardInterrupt:
        exitFlag = 1
    while True:
        data = readData()

        if data == None:
            continue

        data = [d * 0.0436 for d in data]

        #print("%.0f, %.0f, %.0f, %.0f"  % (data[d_format['fwd']], data[d_format['bkwd']], data[d_format['left']], data[d_format['right']]))
        if magnet_data:
            print(magnet_data)

        time.sleep(0.1)
    exitFlag = 1
    thread1.join()
    print('Exiting main thread')
