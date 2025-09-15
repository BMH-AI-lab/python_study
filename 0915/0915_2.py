# Set 
# 중복되지 않는 요소들의 순서가 없는 집합
# 수학의 집합 개념을 구현한 자료구조 
# 해시 테이블 기반으로 빠른 멤버심 테스트 가능 

# 왜 set이 필요한가?
# 중복 데이터가 필요한 경우 
visitors = ['철수', '영희', '철수', '민수', '영희']

# 리스트로 중복제거(비효율적) O(n) 검색
unique_visitors_list = []
for visitor in visitors:
    if visitor not in unique_visitors_list:
        unique_visitors_list.append(visitor)
     
# set으로 중복제거(효율적) O(1) 검색 
unique_visitors_set = set(visitors)
print(unique_visitors_set)

# 특징
# 1. 순서 없음: 요소들의 순서가 보장되지 않음
# 2. 중복 불가: 같은 값은 하나만 저장  
# 3. 변경 가능: 요소 추가 / 삭제 기능 
# 4. 인덱싱 불가: 순서가 없어 인덱스로 접근 불가능 
# 5. 빠른 검색 O(1) 시간 복잡도로 요소 확인 

# set 생성방법
# 1. 빈 set 생성 
# empty_set = {} # 이것은 딕셔너리 
empty_set  = set()

# 값이 있는 set 생성 
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
fruits = {'사과', '비니니', '오렌지'}

# 리스트 / 튜플에서 set 생성
list_numbers = [11, 2, 13, 5, 4, 3, 2, 4]
set_numbers = set(list_numbers)
print(set_numbers)

# 문자열에서 set 생성 
chars = set('Heelo')
print(chars)

#Comprehension
for i in range(10):
    print(i, end=' ')

com_set = {i for i in range(10)}
print(com_set)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

com_set1 = {i * 2 for i in range(10)}
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(sorted(com_set1))

com_set2 = {(i ** 2 + 1) for i in range(10)}
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(com_set2)

com_set3 = {(i * 3 + 2 - 1) for i in range(10)}
print(com_set3)

com_list = [i for i in range(2, 10, 2)]
# [2, 4, 6, 8]

# 메서드 
colors = {"빨강", "노랑", "파랑"}

colors.add("초록")
print(colors)
colors.update(['보라', '주황'])
print(colors)

colors.update(["검정"], ["하양", "회색"])
print(colors)

colors.remove('검정')
print(colors)

colors.discard('검정')
print(colors)
colors.discard('주황')
print(colors)

poped = colors.pop()
print(poped)
print(colors)


colors.clear()
print(colors)


# 집합연산 
A= {1, 2, 3, 4, 5}
B = {1, 2, 6, 7, 8}

intersection1 = A & B
intersection2 = A.intersection(B)
print("intersection1: ",  intersection1) 
print("intersection2: ", intersection2)

union1 = A | B
union2 = A.union(B)
print("union1: ", union1) 
print("union2: ", union2)

difference1 = A - B
difference2 = A.difference(B)
print("difference1: ", difference1)
print("dofference2: ", difference2)

sym_diff1 = A ^ B
sym_diff2 = A.symmetric_difference(B)
print("sym_diff1: ", sym_diff1)
print("sym_diff2: ", sym_diff2)

A = {1, 2, 3}
B = {3, 4, 5}

A.intersection_update(B)
print("A", A)

A = {1, 2, 3}
A. difference_update(B)
print("A", A)

A = {1, 2, 3}
A. symmetric_difference_update(B)
print("A", A)

A ={1, 2, 3, 4, 5}
B = {1, 2, 3, 4, 5}
C = {6, 7, 8,}
print(A.issubset(B))
print(B.issubset(A))
print(A <= B)

#상위 집합인지 확인 
print(A.issuperset(B)) # False
print(B.issuperset(A)) # True
print(B >= A)

# 진 부분집합 확인 
print(B > A)
print(B < A)

# 서로수 집합 
# 교집합이 없는지 확인
print(A.isdisjoint(C))

#frosenset() (불변집합)
fs1 = frozenset([1, 2, 3, 4])
# 불변이므로 수정 삭제가 불가 
# fs1.add(5) 
# fs1.remove() 
# fs1.discard