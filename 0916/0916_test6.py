secret_code = "codingonre3"
while secret_code:
    user = input("비밀 코드를 입력하세요: ")
    if user == secret_code:
        print("입장완료 환영합니다.")
        exit()
    elif user != secret_code:
        print("비밀번호가 틀렸습니다. 다시 시도해주세요." )