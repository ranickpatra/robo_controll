from smbus2 import SMBusWrapper
import time
import math


def readData():
    with SMBusWrapper(1) as bus:
        try:
            block = bus.read_i2c_block_data(6, 0, 6)
        except:
            print("I2C ERROR")
            return

        for b in block:
            if b & 0xFF == 0xFF:
                return
        data = []
        data.append(block[0] << 8 | block[1])
        data.append(block[2] << 8 | block[3])
        data.append(block[4] << 8 | block[5])
        return tuple(data)

if __name__ == '__main__':
    while True:
        x, y, z = readData()
        print(x, y, z)
        time.sleep(0.2)
