# 문제 3. 사용자 정보 출력 함수
def information(**kwargs):
    for key, value in kwargs.items():        
        print(f"{key} : {value}")
information(name= "김철수", age = 20, email = "python@naver.com")

# 문제 4. 할인 계산기

def mart(**kwargs):
    for key, value in kwargs.items():
        a = value * 0.9
        print(f"{key}: {int(a)}")
    
    return mart
     
mart(라면=3500, 깁밥=2000, 아이스아메리카노=2000)