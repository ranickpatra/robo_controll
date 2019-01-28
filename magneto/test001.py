import qmc5883l
import math

mag_sens = qmc5883l.QMC5883L()


[x, y, z] = mag_sens.get_magnet()

print(math.degrees(math.atan(y/x)))
