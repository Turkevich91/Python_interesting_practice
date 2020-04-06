# def man():
    #read file
file = open("yesno.txt", "r")
lines = file.readlines()
file.close()

#look for patterns
countYes = 0
countNo = 0
for line in lines:
    line = line.strip().upper()
    #print(line)
    if line.find("YES") != -1:
        countYes = countYes + 1
    if line.find("NO") != -1:
        countNo = countNo +1

    #display result
print("Yes: ", countYes)
print("No: ", countNo)

# man()