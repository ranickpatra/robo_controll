import py_qmc5883l
import time
import math

sensor = py_qmc5883l.QMC5883L()

while True:
    [x, y, z] = sensor.get_magnet()
    deg = math.degrees(math.atan2(y, x))
    print(deg)
    time.sleep(0.1)
