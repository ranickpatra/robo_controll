import py_qmc5883l
import time
import math

sensor = py_qmc5883l.QMC5883L()

while True:
    [x, y, z] = sensor.get_magnet()
    print(math.degrees(math.atan2(y, x)))
    time.sleep(0.1)
