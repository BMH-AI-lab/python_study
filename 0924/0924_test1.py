user_name1, user_pass1 = input("이름과 비밀번호를 입력하세요: ").split(",")
user_name2, user_pass2 = input("이름과 비밀번호를 입력하세요: ").split(",")
user_name3, user_pass3 = input("이름과 비밀번호를 입력하세요: ").split(",")

with open('member.txt', 'w', encoding ='utf-8') as f:
    f.write(f"User1의 이름: {user_name1}, user1의 비밀번호: {user_pass1}\n")
    f.write(f"User2의 이름: {user_name2}, user2의 비밀번호: {user_pass2}\n")
    f.write(f"User3의 이름: {user_name3}, user3의 비밀번호: {user_pass3}\n")

with open('member.txt', 'r', encoding ='utf-8') as f:
    content = f.read()
    print(content)