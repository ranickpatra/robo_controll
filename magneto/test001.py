import qmc5883l

mag_sens = qmc5883l.QMC5883L()


data = mag_sens.get_magnet()

print(data)
