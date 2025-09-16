# 문제 1. 딕셔너리 핵심 개념 통합 실습
user = dict()
user.update({"username": "skywalker", "email": "sky@example.com", "level": 5})
email_value = user["email"]
print("email 값 읽기: ", email_value)
user["level"] = 6
print("level 수정한 값: ", user["level"])
print(user.get("phone", "미입력"))
user.update({"nickname": "sky" })
print("nickname 추가: ", user)
user.pop('email')
print('email 항목 삭제 결과: ', user)
user.setdefault("signup_date", '2025-07-10')
print("sign_date 키 추가 결과(최종 user 딕셔너리): ", user)

