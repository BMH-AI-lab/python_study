# 문제1. UserAccount클래스 : 비밀번호 보호
class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def change_password(self, old_pw, new_pw):
        if self.__password == old_pw:
          self.__password = new_pw
          print("비밀번호가 변경되었습니다.", self.__password)
        else:
           print("비빌번호 불일치")

    def check_password(self, password):
        return self.__password == password

user1 = UserAccount("홍길동", "python123")
print("비밀번호 일치 여부: ", user1.check_password('python456'))
print("비밀번호 일치 여부: ", user1.check_password('python123'))

user1.change_password("python3210", "python3210")
user1.change_password("python123", "python3210")



