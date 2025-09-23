# 문제 1. Shape 클래스 오버라이딩

class Shape:
    def __init__(self, sides, base):
        self.sides = sides
        self.base = base

    def printInfo(self):
        print(f"변의 개수: {self.sides}")
        print(f"밑변의 길이: {self.base}")

    def area(self):
        print("넓이 계산이 정의되지 않았습니다.")

class Rectangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height

    def area(self):
        print(f"area: {self.base} x {self.height} = {self.base} * {self.height}")
    
class Triangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height

    def area(self):
        print(f"area: {self.base} x {self.height} / 2 = {self.base} * {self.height} / 2")



shape = [Rectangle(4, 4, 6), Triangle(4, 6, 7)]
for i in shape:
    i.printInfo()
    i.area()