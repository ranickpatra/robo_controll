from smbus2 import SMBusWrapper
import sys

address = 0x06


while True:
    data = [0, 200]
    try :
        data[0] = int(input("Enter 0, 1, 2, 3, 4 :: "))
    except KeyboardInterrupt:
        print("\nexit")
        sys.exit()
    except :
        data[0] = 0

    #if data[0] > 4 :
    #    data[0] = 0
    print(data)
    with SMBusWrapper(1) as bus:
        bus.write_i2c_block_data(address, 0, data)
        #block = bus.read_i2c_block_data(address, 0, 2)
        #print(block)
