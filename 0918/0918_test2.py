a = int(input("숫자를 입력하세요: "))
b = int(input("숫자를 입력하세요: "))
operator = input("연산자를 입력해주세요: ")

def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b 
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        print("지원하지 않는 연산입니다.")     
    return calculate

print(calculate(a, b, operator))
