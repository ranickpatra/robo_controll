from smbus2 import SMBusWrapper
#import sys

address = 0x06

def send(data):
    data = [data, 200]

    if data[0] > 4 :
        data[0] = 0
    #print(data)
    with SMBusWrapper(1) as bus:
        try:
            bus.write_i2c_block_data(address, 0, data)
        except:
            pass
        #block = bus.read_i2c_block_data(address, 0, 2)
        #print(block)
