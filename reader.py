import re

f = open("19042p04.sum", "r")
line = f.readline()
while line:
    # S = line.replace(':', '').split('x')


    # print(S)
    line = f.readline()

    intab = ':Xx'
    outtab = '   '
    res = line.translate(line.maketrans(intab, outtab))
    print(res)
f.close()
print(line())