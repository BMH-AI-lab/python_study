# 문제 1. 중복 제거 및 개수 세기 
submissions = ['kim', 'lee', 'kim', 'park', 'choi', 'lee', 'lee']
submissions1 = set(submissions)
print("제출한 학생 수: ", len(submissions1))
print("제출자 명단: ",submissions1)

# 문제 2. 공동 관심사 찾기 
user1 = {'SF', 'Action', 'Drama'}
user2 = {'Drama', 'Romance', 'Action'}

print("공통 관심 장르: ", user1 & user2)
print("서로 다른 장르: ", user1 ^ user2)
print("잔체 장르: ", user1 | user2)

#문제 3. 부분집합 관계 판단
my_certificates = {'SQL', 'Python', 'Linux'}
job_required = {'SQL', 'Python'}

print("지원 자격 충족 여부: ", my_certificates.issuperset(job_required))