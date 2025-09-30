# 문제 3: 1부터 n까지의 합 
def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n-1)
    # return sum(range(1, n+1))
    
print(sum_to_n(5))


# 문제 5. 문자열 뒤집기 
def reverse_string(s):
    if len(s) <= 0:
        return s
    return reverse_string(s[1:len(s)]) + s[0]

print(reverse_string("hello"))