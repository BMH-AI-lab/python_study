login_id = "python_123"
login_password = "123456"
while True:
    user_id = input("아이디를 입력하세요: ")
    if user_id != login_id:
        print("ID가 존재하지 않습니다.")
    else:
        pass
        while True:    
            user_pass = input("비밀번호를 입력하세요: ")
            if user_pass == login_password:
                print("로그인 성공!!")
                exit()
            elif user_pass != login_password:
                print("비밀번호가 틀렸습니다.") 
                