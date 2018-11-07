import sys
length = 0

def Cprint(data):
    global length
    l = sys.stdout.write(str(data))
    if l > length:
        lenght = l
    sys.stdout.write(" "*(length-l))
    sys.stdout.flush()
    sys.stdout.write("\b"*length)
