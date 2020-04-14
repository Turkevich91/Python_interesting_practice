f = open("19042p04.sum", "r")
line = f.readline()
while line:
    print(line.replace(':', "").split())
    line = f.readline()
f.close()
print(line())