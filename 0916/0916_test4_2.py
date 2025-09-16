# 문제3. 3의 배수의 합 구하기
sum=0
for i in range(1, 101):
    if i % 3 == 0:
        sum += i 
print(f"3의 배수 합은 {sum}" )

# 문제4. 짝수이면서 5의 배수인 수 출력하기

number = int(input("숫자를 입력하세요: "))
for i in range(1, number+1):
    if i % 2 == 0 and i % 5 == 0:
        print(i) 