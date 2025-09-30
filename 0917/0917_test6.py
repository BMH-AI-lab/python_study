# 문제2. 유효한 나이만 평균 내기
times = 0
sum_age =0
while times < 5:
    age = int(input("나이를 입력하세요: "))
    if age >= 0 and age <= 120:
        sum_age += age
        times += 1
    

print(f"총 나이의 합계는{sum_age}, 평균은 {sum_age/5}입니다.")  
