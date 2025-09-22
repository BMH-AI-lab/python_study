# 문제 2. Student 클래스: 성적 검증(@property 사용)

class Student:
    def __init__(self, name):
       self.name = name
       self.__score = 0

    @property
    def score(self):
       return self.__score
    
    @score.setter
    def score(self, value):
        if  0  <= value <= 100:
          self.__score = value
        else:
          raise ValueError("범위를 넘었습니다.")
        
s =  Student("김철수")
s.score = 80
print(f"{s.name}님의 점수: {s.score}")
s.score = 130
print(s.score)

       


