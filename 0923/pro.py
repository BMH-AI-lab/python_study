def solution(n):
    answer = []
    for i in range(n, n+1):
        if i // n == 0:
            i += 1
    return sorted(answer)


solution(24)