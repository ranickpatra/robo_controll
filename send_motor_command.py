from smbus2 import SMBusWrapper
import sys

address = 0x06


while True:
    try :
        data = int(input("Enter 0, 1, 2, 3, 4 :: "))
    except KeyboardInterrupt:
        print("\nexit")
        sys.exit()
    except :
        data = 0

    if data > 4 :
        data = 0
    #data = data << 8 | 200;
    with SMBusWrapper(1) as bus:
        bus.write_byte(address, data)
        bus.write_byte(address, 150)
		#ok
