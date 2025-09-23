from random import randint

game_list = ["가위", "바위", "보"]
user = input("'가위', '바위', '보' 중 하나를 입력하세요: ")
print(f"사용자 입력: {user}")

user_list = game_list.index(user)
computer_list = randint(0, 2)

print(f"컴퓨터 입력: {game_list[computer_list]}")

if user_list == computer_list:
    print("무승부")
elif game_list[user_list -1] == game_list[computer_list]:
    print("승리")
else:
    print("패배")
