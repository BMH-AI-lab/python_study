import copy

scores = {
    "김철수" : 85, "이영희": 92, "박민수": 78
}

scores.setdefault('정수진', 88) # 새로 추가 
scores.setdefault('김철수', 100)
print(scores)

scores_copy = scores.copy()
scores_copy['최동훈'] = 95
print('scores', scores)
print()
print('scores_copy', scores_copy)

# decopy() -깊은 복사 
nested_dict = {
    "team1": {'leader': "김철수", 'members': ['이영희', '박민수']}, 
    "team2": {'leader': "정수진", 'members:': ['최종훈', '강미나']}
            }
shallow = nested_dict.copy()
deep = copy.deepcopy(nested_dict)
nested_dict['team1']['members'].append('신입')
print('shallow: ', shallow["team1"]["members"])
print()
print('deep: ', deep["team1"]["members"])



print()
print()
print()
print()
print()
print()
print()










