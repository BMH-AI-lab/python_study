# 문제1. 입력 받은 수의 합 구하기
n = int(input("숫자를 입력하세요: "))
for i in range(1):
    s = n * (n + 1) // 2
    print("1부터 사용자가 입력한 수까지의 합: ", s)

print()

# 문제2. 구구단 만들기(1)
dan = int(input("출력하고 싶은 단을 입력하세요: "))
for a in range(1, 10):
    print(f'{dan} * {a} = {dan * a}')