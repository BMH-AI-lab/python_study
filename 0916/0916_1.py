# 딕서너리(Dictionary)
# 하나의 키(Key)와 값(value)을 쌍으로 묶어 데이터를 저장하는 자료형 
# 해시 테이블 기반으로 매우 빠른 검색 속도 
# python의 가장 강력하고 유용한 자료구조 중 하나 

student_ids =  ["20230001", "20230002", "20230003"]
student_names = ["김철수", "이영희", "박민수"]

# 특정 학번의 이름을 찾으려면?
target_id = "2023002"
if target_id in student_ids:
    Index = student_ids.index(target_id) #O(n)
    name = student_names[Index]
    print(name) 

#딕셔너리를 사용하는 경우- 직관적이고 빠름
students = {"2023001": "김철수", "2023002": "이영희", "2023003": "박민수"}
print(students["2023002"]) #O(1) - 즉시 접근 가능 


# 특징 
# Key-value 쌍: 각 값에 고유한 키로 접근 
# 빠른 검색: O(1) 시간복잡도
# 변경 가능 (Mutable): 요소 추가, 수정, 삭제 가능 
# Key는 유일: 중복 키 불가(값은 중복 가능)
# 순서 보장: python3.7 + 부터 삽입 순서 유자


#Dictionary 생성
# 1. 빈 딕셔너리 생성
empty_dict = {} # dict
print(type(empty_dict))


# 값이 있는 딕셔너리 생성
person = {"name": '김철수', 'age': 25, 'city': 'seoul'}
print('person', person)

# dict() 생성자 사용
person2 = dict(name = '이영희', age = 25, city ="부산")
print('person2', person2)

# 4. 리스트/튜플로부터 생성 
pairs = (('a', 1), ('b', 2))
dict_fron_pairs = dict(pairs)
print('dict_fron_pairs', dict_fron_pairs)

# 5. zip()를 이용한 생성 
keys =  ['name', 'age', 'city']
Values = ['박민수', 21, '대전']
person3 = dict(zip(keys, Values))
print("person3", person3)

# 6. dictionary comprehension
squres = {x: x**2 for x in range(1, 6)}
print('squars', squres)


# 7. fromkeys() 메서드  
key = ['a','b', 'c']
default_dict = dict.fromkeys(key, 'A')
print('default_dict', default_dict)

# key로 사용가능한 타입 
# Hashable 타입만 key로 사용 가능 
# valid_dict = {1: '정수',
#             3.14: '실수', 
#             (1, 2): "튜플", 
#             True: "불리언", frozenset: "Frozenset"} 
# 
# 접근과 수정 
student = {
    'name': '김철수', ''
    'age': 20, 
    'major': "컴퓨터 공학" ,
    'gpa': 3.7
}

name = student['name']
print('name', name)

major = student.get('major')
print('major', major)
grade1 = student.get('grade')
print('grade', grade1)

grade2 = student.get('grade', 'N/A')
print('grade2', grade2)



# keys() values(), items()
print('students.keys()', list(students.keys()))
print('students.values()', list(students.values()))
print('students.items()', list(students.items()))

# 값 수정, 추가 
student = {
    'name': '김철수', ''
    'age': 20, 
    'major': "컴퓨터 공학" ,
    'gpa': 3.7
}

student['age'] = 23
print("student", student)
student['grade'] = 3
print("student", student)

# update() 메서드로 여러 값 한번에 변경가능
student.update({'gpa': 4.0, "city": "seoul", 
                'email': 'rtha@gmail.com'})
print("student", student)

# 값 삭제 
del student['grade']
print("student", student)

# pop() 메서드 값을 변환하면서 삭제 
poped = student.pop('city')
print("poped", poped)
print("student", student)

#popitem 마지막 항목 제거 
lastitem = student.popitem()
print('lastitem', lastitem)

student.clear()
print('student', student)
# 
# 





