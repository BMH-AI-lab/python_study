# 실습4. 거듭 제곱
def power_num(a, b):
    if b == 0:
        return 1
    return a * power_num(a, b - 1)

print(power_num(2, 3))


# 실습 5. 팩토리얼(Factorial)
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result
print(factorial(5))

# 실습 6. 피보나치 수열(Fibonacci Numbers)
def fibonacci(n):
    result = 1
    for i in range(n, n+1):
        if n <= 1:
            return n
    return fibonacci(n-1) + fibonacci(n-2)



