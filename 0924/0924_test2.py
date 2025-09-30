login_name = input("이름을 입력하세요: ")
login_password = input("비밀번호를 입력하세요: ")


with open('member.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if login_name in line and login_password in line:
                print("로그인 성공")
                break  
        else:
            print("로그인 실패")
            break  
