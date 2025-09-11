food = input("식품을 입력하세요: ")

if food == "김밥":
    money = int(input("금액을 입력하세요: "))
    if money < 2500:
        print("금액이 부족합니다.")
    elif money == 2500: 
        print("구매성공!!!")
    elif money >= 2500: 
        print("금액을 잘못 입력했습니다.")

if food == "삼각김밥":
    money = int(input("금액을 입력하세요: "))
    if money < 1500:
        print("금액이 부족합니다.")
    elif money == 1500: 
        print("구매성공!!!")
    elif money >= 1500: 
        print("금액을 잘못 입력했습니다.")

if food == "도시락":
    money = int(input("금액을 입력하세요: "))
    if money < 4000:
        print("금액이 부족합니다.")
    elif money == 4000: 
        print("구매성공!!!")
    elif money >= 4000: 
        print("금액을 잘못 입력했습니다.")
else: 
    print("잘못 입력했습니다.")