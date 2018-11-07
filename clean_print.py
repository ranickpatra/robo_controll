import sys
lenght = 0

def Cprint(data):
    global length
    l = sys.stdout.write(str(data))
    if l > lenght:
        lenght = l
    sys.stdout.write(" "*(lenght-l))
    sys.stdout.flush()
    sys.stdout.write("\b"*lenght)
