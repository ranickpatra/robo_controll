import sys

def Cprint(data, lenght=80):
    l = sys.stdout.write(str(data))
    sys.stdout.write(" "*(length-l))
    sys.stdout.flush()
    sys.stdout.write("\b"*lenght)
