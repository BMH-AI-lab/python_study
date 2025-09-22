class Rectangle: 
    def __init__(self,  width, height):
        self.width =  width
        self.height = height
      

    def area(self): 
        area_answer = self.width * self.height
        return area_answer


w = int(input("너비를 쓰시오: "))
h = int(input("높이를 쓰시오: "))

num_area = Rectangle(w, h)
print()
print(f"사각형의 넓이:", num_area.area())