from smbus2 import SMBusWrapper
import time
import numpy as np
import queue

address = 0x0D
max_queue_size = 8

x_queue = queue.Queue(maxsize=max_queue_size)
y_queue = queue.Queue(maxsize=max_queue_size)
z_queue = queue.Queue(maxsize=max_queue_size)



with SMBusWrapper(1) as bus:
    bus.write_byte_data(address, 9, 29)

def readData():
    with SMBusWrapper(1) as bus:
        data = []
        for i in range(3):
            data.append((bus.read_byte_data(address, i*2) << 8 | bus.read_byte_data(address, i*2+1)))

        data = np.asarray(data, dtype="int16")
        if x_queue.qsize() == max_queue_size:
            x_queue.get()

        x_queue.put(data[0])

        if y_queue.qsize() == max_queue_size:
            y_queue.get()

        y_queue.put(data[1])

        if z_queue.qsize() == max_queue_size:
            z_queue.get()

        z_queue.put(data[2])

        if x_queue.qsize() != max_queue_size or y_queue.qsize() != max_queue_size or z_queue.qsize() != max_queue_size :
            return


        print(int(sum(x_queue.queue) / x_queue.qsize()))

        



while True:
    readData()
    time.sleep(0.01)

