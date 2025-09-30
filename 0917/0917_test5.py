# 문제2. 업다운 게임
import random

print("1~100사이 무작위 수를 생성 중입니다.")
n = 0
count = 0
random_value = random.randrange(1, 101)   
n = int(input("1부터 100 사이 숫자를 입력해 주세요: "))
while random_value != n:
    if n > 0 and n < 101:
        if n < random_value:
            print(f"{n}보다는 커요.")
        else:
            print(f"{n}보다는 작아요.") 
    else:
        print("다시 입력해주세요.")
    count += 1 
    n = int(input("1부터 100 사이 숫자를 입력해 주세요: "))
print(f'{count}번만에 정답을 맞췄습니다.')    
                          

