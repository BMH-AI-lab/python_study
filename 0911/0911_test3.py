age = int(input("나이를 입력해주세요: "))

if age <= 12:
    print("전체관람가")
elif 13 <= age <= 15:
    print("12세 이상 관람가")
elif 16 <= age <= 18:
    print("15세 이상 관람가")
else:
    print("청소년 관람불가 가능")
    