from smbus2 import SMBusWrapper
import time
import sys

address = 0x05

def readData():
    with SMBusWrapper(1) as bus:
        try:
            block = bus.read_i2c_block_data(address, 0, 8)
        except:
            print("I2C ERROR while reading")
            return

        for b in block:
            if b & 0xFF == 0xFF:
                return
        data = []
        data.append(block[0] << 8 | block[1])
        data.append(block[2] << 8 | block[3])
        data.append(block[4] << 8 | block[5])
        data.append(block[6] << 8 | block[7])
        l = sys.stdout.write(str(data))
        sys.sdtout.write(" "*(40-l))
        sys.stdout.flush()
        sys.stdout.write("\b"*40)


while True:
    readData()
    time.sleep(0.1)
