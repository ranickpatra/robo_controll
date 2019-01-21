from smbus2 import SMBusWrapper
import sys

address = 0x06


while True:
    data = [0, 100]
    try :
        data[0] = int(input("Enter 0, 1, 2, 3, 4 :: "))
    except KeyboardInterrupt:
        print("\nexit")
        sys.exit()
    except :
        data[0] = 0

    if data[0] > 4 :
        data[0] = 0

    with SMBusWrapper(1) as bus:
        bus.write_byte(address, d[0])
