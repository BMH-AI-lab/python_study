def solution(s):
    answer = True
    # 스택이라는 빈 리스트 생성 
    stack = []
    for i in s:
        # i가 '('이면 스택 추가 
        if i == '(':
            stack.append(i)
        # i가 ')' 이면 스택 제거 
        # 그안에 스택의 올바른 괄호가 아니면 False
        elif i == ')':
            if not stack:
                return False
            stack.pop()
    # 제대로 된 괄호가 아니면 False
    if stack:
        return False
    # 제대로 된 괄호이면 True
    else:
        return True



# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

















































































