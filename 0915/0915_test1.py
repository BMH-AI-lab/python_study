# Step 1. 손상된 고객 정보 복원하기
user = ("minji", 25, "Seoul")
list_user = list(user)
list_user[0] = "eunji"
restored_user = tuple(list_user)
print(restored_user)
# Step 2. 고객 정보 언패킹하여 변수에 저장
for i in range(0, len(restored_user)):
    if i == 0:
        name = restored_user[0]
    elif i == 1:
        age = restored_user[1]
    if i == 2:
        city = restored_user[2] 

print(f"name: {name}, age: {age}, city: {city} ")   

# Step 3. 지역별 보안 정책 분기 처리
if city == "Seoul":
    print("서울 지역 보안 정책 적용 대상입니다.")
else:
    print("일반 지역 보안 정책 적용 대상입니다.")

# Step 4. 고객 데이터 통계 분석
users = ("minji", "eunji", "soojin", "minji", "minji")

count1 = users.count('minji')
print("minji라는 이름 갯수", count1)
index1 = users.index('soojin')
print("soojin이 처음 등장하는 위치", index1)

# Step 5. 고객 이름 정렬
sorted_users = sorted(users)
print("users 튜플을 정렬한 결과: ", sorted_users)
