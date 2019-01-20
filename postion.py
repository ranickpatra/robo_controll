from smbus2 import SMBusWrapper
import time
import sys
from clean_print import Cprint

#length = 455 cm
#width = 149 cm

#data :: R, F, L, B
#        1, 2, 4, 3
d_format = {'fwd' : 1, 'bkwd' : 3, 'left' : 2, 'right' : 0}

address = 0x05
width = 0
height = 0
pos = {'x':0, 'y':0}

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


if __name__ == '__main__':
    while True:
        data = readData()

        if data == None:
            continue

        data = [d/2 * 0.034 for d in data]

        print(data)

        time.sleep(0.1)
