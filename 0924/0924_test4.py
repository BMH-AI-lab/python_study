def get_age_group():
    while True:
        try:
            age = int(input("나이를 입력하세요: "))
            if 0 <= age < 20:
                print("미성년자")
            elif 19 <= age < 40:
                print("청년")
            elif 40 <= age < 60:
                print("중년") 
            elif 60 <= age < 150:
                print("노년")
            else:
                print("범위를 초과 했습니다.")
                break
          
    
        except ValueError:
            print("숫자를 입력해주세요.") 
        except IndexError:
            print("인덱스 범위를 초과했습니다.")



# 테스트
get_age_group()