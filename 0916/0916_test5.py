numbers = 100
while numbers :
    number = int(input(""))
    for i in range(1, 101):
        i = number
        if i < numbers:
            print("입력한 숫자보다 작아요")
        elif i > numbers:
            print("입력한 숫자보다 커요")
        elif i == numbers:
            print(f"{''} 만에 정답을 맞췄습니다.")
        exit()
     