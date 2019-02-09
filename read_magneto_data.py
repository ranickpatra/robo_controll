import py_qmc5883l
import time

sensor = py_qmc5883l.QMC5883L()

while True:
    [x, y, z] = sensor.get_magnet()
    print(x, y, z)
    time.sleep(0.1)
