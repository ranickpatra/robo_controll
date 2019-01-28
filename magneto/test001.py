import qmc5883l
import math
import time

mag_sens = qmc5883l.QMC5883L()

while True:
    [x, y, z] = mag_sens.get_magnet()
    print(x, y, z)
    time.sleep(0.2)
