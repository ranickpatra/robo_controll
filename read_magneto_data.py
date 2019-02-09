import py_qmc5883l
import time
import math

sensor = py_qmc5883l.QMC5883L()

while True:
    [x, y, z] = sensor.get_magnet()
    if y > x:
        deg = math.degrees(math.atan2(y, x))
    else:
        deg = 90 - math.degrees(math.atan2(x, y))
    print(deg)
    time.sleep(0.1)
