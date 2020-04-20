# import re
parts, nest, layout = [], [], []
f = open(r"19042p04.sum", "r")
line = f.readline()
while line:
    S = line.replace(':', "").split()
    # print(S)
    if line == '\t*** PART SUMMARY ***\n':
        print('@'*50 + '\n' + '\t'*5 + 'Part list\n' + '@'*50)
        f.readline()    # Просто пропускает одну строку бесполезных данных
        line = f.readline()     # начиная с этой строки и дальше данные проверяются и записываются
        while line != '\n':
            S = line.replace(':', "").split()
            S[1], S[2], S[3] = float(S[1]), float(S[2]), int(S[3])
            parts.append(S)
            print(S[0], '\t\t', S[1], '\t\t', S[2], '\t', S[3])
            line = f.readline()

    if line.startswith('\t*** Layout Number ') & line.endswith(' ***\n'):
        line = f.readline()
        while line != '\n':
            pass

        line = f.readline()
        while line != '\n':
            pass

    line = f.readline()

f.close()

