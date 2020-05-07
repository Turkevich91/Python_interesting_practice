from pyautocad import Autocad, APoint
import math


def limit_Of_Borders(num, flag):
    step = 1
    if flag and flag < diameter:
        num += step
        if num == diameter:
            flag = False
        return num, flag
    else:
        num -= step
        if num == 0:
            flag = True
        return num, flag


acad = Autocad(create_if_not_exists=True, visible=True)
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)

diameter = 1000

p1 = APoint(0, 0)
p2 = APoint(diameter / 2, 0)
p1.y = diameter / 2

flagY = True
flagX = True
for i in range(diameter * 2):
    text = acad.model.AddText('Circle %s' % i, p1, 0.5)
    acad.model.AddLine(p1, p2)
    acad.model.AddCircle(p1, 10)

    p1.y, flagY = limit_Of_Borders(p1.y, flagY)
    p1.x, flagX = limit_Of_Borders(p1.x, flagX)
