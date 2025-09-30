import numpy as np

# 문제 4
arr = np.array([[95, 97],
                [80, 85]])

max_n = 100 - arr

result = arr + max_n
print("최대값 100으로 만들기 위해 필요한 값을 더한 결과: \n", result)
print()

# 문제 5
arr = np.array([[1, 2, 3], [4, 5, 6]]) 

result1 = arr[0] * 10
print("2차원 배열에서 각 행에 다른 값을 곱하여 만든 배열: ")
print(result1)
result2 = arr[1] * 100
print(result2)
print()

# 문제 6
arr = np.array([[10, 20], 
                [30, 40],
                [50, 60]])

arr_1 = np.array([[100],
                 [200],
                 [300]])

print("각 행마다 다른 스칼라 값을 더한 결과: \n", (arr + arr_1))