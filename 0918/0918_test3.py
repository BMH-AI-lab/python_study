# 문제 1. 숫자 여러 개의 평균 구하기
def avg_all(*args):
    return sum(args) // len(args) 
print("평균값: ", avg_all(1, 2, 3, 4, 5))

# 문제 2. 가장 긴 문자열 찾기(max 함수에 대해 찾아보고 풀기)
def string_a(*args):
    long_string = max(args, key=len) 
    print("긴문자열: ", long_string)
    return long_string
string_a('python', 'codingon', "inchon")

