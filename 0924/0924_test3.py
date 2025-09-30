def saved_phone(input_id):
    phone_num = input("전화번호를 입력하세요: ")
    members = {}

    try:
        with open('member_tel.txt', 'a', encoding='utf-8') as f2:
                  for line in f2:
                       saved_name, saved_phone = line.strip().split()
                       member[saved_name] = saved_name
             member[login_name] = phone_num
    member[login_name] = phone_num

with open('member.txt', 'r', encoding='utf-8') as f:
    login_name = input("이름을 입력하세요: ")
    login_password = input("비밀번호를 입력하세요: ")
    for line in f:
        user_id, user_pw = line.strip().split()
        if user_id == login_name and user_pw == login_password:
                print("로그인 성공")
                phone_num = input("전화번호를 입력하세요: ")
                member = {}
                with open('member_tel.txt', 'a', encoding='utf-8') as f2:
                     for line in f2:
                          saved_name, saved_phone = line.strip().split()
                          member[saved_name] = saved_name
                member[login_name] = phone_num

                with open('member_tel.txt', 'w', encoding='utf-8') as f3:
                     
                break  
        else:
            print("로그인 실패")
            break  
