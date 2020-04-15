#import re
parts = []

f = open("19042p04.sum", "r")
line = f.readline()
while line:
    S = line.replace(':', "").split()
    print(S)
    if line == '\t*** PART SUMMARY ***\n':
        line = f.readline()
        line = f.readline()
        while line != '\n':
            S = line.replace(':', "").split()
            print(S[0[0]])
            parts.append(S)
            # parts.append(S[0], float(S[1]), float(S[2]), int(S[3]))
            # parts[1,2]= float(parts[1]), float(parts)
            line = f.readline()

    line = f.readline()
f.close()
# print(line)
for x in len(parts):
    print(parts[x])


# intab = ':Xx'
# outtab = '   '
# res = line.translate(line.maketrans(intab, outtab))
# print(res)

