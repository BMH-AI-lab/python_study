import math 

x1, y1 = int(input("첫 번재 x값: ")), int(input("첫 번재 y값: "))
x2, y2 = int(input("두 번재 x값: ")), int(input("두 번재 y값: "))


p = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
print(round(p, 2))
