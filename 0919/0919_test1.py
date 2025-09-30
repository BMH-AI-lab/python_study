# 로그인/로그아웃 전역 상태 관리 
current_user = ""

def login(name):
    global current_user

    if current_user == "":
        current_user = name
        print(f"{name}님 로그인 성공")
    else:
        print("이미 로그인되어 있습니다")


def logout():
    global current_user
    current_user = ""
    print("로그아웃되었습니다.")

login("Ian")
login("CodingOwl")
logout()
login("CodingOwl")
print(current_user)