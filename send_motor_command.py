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

    with SMBusWrapper(1) as bus:
        bus.write_byte_data(address, 0, data)
        #bus.write_byte_data(address, 0, 200 & 0xFF)
		#ok
