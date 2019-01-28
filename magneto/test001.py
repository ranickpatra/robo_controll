import qmc5883l
import math
import time

mag_sens = qmc5883l.QMC5883L()

while True:
    [x, y, z] = mag_sens.get_magnet()
    direc = math.atan(y/x) * 180 / math.pi
    print("{:.4f}, {:.4f}, {:.4f} {:.2f}".format(x, y, z, direc))
    time.sleep(0.2)
