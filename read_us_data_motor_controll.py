from smbus2 import SMBusWrapper
import time

address = 0x05

def readData():
    with SMBusWrapper(1) as bus:
        try:
            block = bus.read_i2c_block_data(address, 0, 8)
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
        data.append(block[6] << 8 | block[7])
        print(data)

    if data[0] < 600:
        send_motor_command(2)
    elif data[1] < 600:
        send_motor_command(1)
    else:
        send_motor_command(0)



def send_motor_command(data=0):
    with SMBusWrapper(1) as bus:
        try:
            bus.write_byte_data(address, 0, data)
        except:
            print("Motor command error")


while True:
    readData()
    time.sleep(0.1)