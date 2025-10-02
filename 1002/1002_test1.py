# 실습 2. DataFrame 연습
import pandas as pd

# 문제 1
data = pd.DataFrame([['홍길동', 28, '서울'], 
                    ['김철수', 33, '부산'],
                    ['이영희', 25, '대구']], columns = ['이름', '나이', '도시'])
print("=== 컬럼명을 '이름', '나이', '도시'로 지정 결과 ===")
print()
print(data)

# 문제 2
dict_data = pd.DataFrame([{'A': [1, 2, 3], 'B': [4, 5, 6]}])
print("=== 딕셔너리로 DataFrame을 생성 결과 ===")
print()
print(dict_data)

# 문제 3
sub_data1 = pd.DataFrame([{'과목': '수학', '점수': 90}, 
                         {'과목': '영어', '점수': 85},
                         {'과목': '과학', '점수': 95}])
print("=== DataFrame 생성 ===")
print()
print(sub_data1)

# 문제 4
sub_data1 = pd.DataFrame([{'과목': '수학', '점수': 90}, 
                         {'과목': '영어', '점수': 85},
                         {'과목': '과학', '점수': 95}])
sub_data2 = pd.DataFrame({'이름': ['민수', '영희', '철수'], '점수': [80, 92, 77]})
result = pd.concat([sub_data1, sub_data2], axis=1)
result.index = ['학생1', '학생2', '학생3'] 
print("=== 인덱스를 ['학생1', '학생2', '학생3']으로 지정한 결과 ===")
print()
print(result)