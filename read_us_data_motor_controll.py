from smbus2 import SMBusWrapper
import time

address = 0x05
motor_triggers = [False, False, False, False]
prev_command = 0
sensor_pos = [3,1, 2, 0]

#data :: R, F, L, B
#        1, 2, 4, 3
d_format = {'fwd' : 1, 'bkwd' : 3, 'left': 2 , 'right' : 0}

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

    # if data[0] < 600:
    #     send_motor_command(2)
    # elif data[1] < 600:
    #     send_motor_command(1)
    # else:
    #     send_motor_command(0)

    for i in range(4):
        motor_triggers[i] = data[i] < 600



    send_motor_command()



def send_motor_command():

    global prev_command
    data = 0
    #data :: F, B, L, R
    #        1, 2, 4, 3
    if motor_triggers[sensor_pos[0]] and motor_triggers[sensor_pos[1]] and motor_triggers[sensor_pos[2]] and motor_triggers[sensor_pos[3]]:
        data = 0
    elif motor_triggers[sensor_pos[0]] and motor_triggers[sensor_pos[1]] and motor_triggers[sensor_pos[2]]:
        # Rotate Right
        data = 3
    elif motor_triggers[sensor_pos[0]] and motor_triggers[sensor_pos[1]] and motor_triggers[sensor_pos[3]]:
        # Rotate left
        data = 4
    elif motor_triggers[sensor_pos[1]] and motor_triggers[sensor_pos[2]] and motor_triggers[sensor_pos[3]]:
        # move forword
        data = 1
    elif motor_triggers[sensor_pos[0]] and motor_triggers[sensor_pos[2]] and motor_triggers[sensor_pos[3]]:
        # move backword
        data = 2
    elif motor_triggers[sensor_pos[0]] and motor_triggers[sensor_pos[1]]:
        #stop
        data = 0
    elif motor_triggers[sensor_pos[2]] and motor_triggers[sensor_pos[3]]:
        #contimue what is previous command
        data = prev_command
    elif motor_triggers[sensor_pos[0]] and motor_triggers[sensor_pos[2]]:
        # Rotate Right
        data = 3
    elif motor_triggers[sensor_pos[0]] and motor_triggers[sensor_pos[3]]:
        # Rotate Left
        data = 4
    elif motor_triggers[sensor_pos[1]] and motor_triggers[sensor_pos[2]]:
        # Move Forword
        data = 1
    elif motor_triggers[sensor_pos[1]] and motor_triggers[sensor_pos[3]]:
        # Rotate Forword
        data = 1
    elif motor_triggers[sensor_pos[0]]:
        data = 0
    else:
        # stop
        data = 1

    prev_command = data;
    with SMBusWrapper(1) as bus:
        try:
            bus.write_byte_data(address, 0, data)
        except:
            print("Motor command error")

if __name__ == '__main__':
    while True:

        try :
            readData()
        except KeyboardInterrupt:
            print("\nexit")
            with SMBusWrapper(1) as bus:
                bus.write_byte_data(address, 0, 0)
            sys.exit()
        time.sleep(0.1)
