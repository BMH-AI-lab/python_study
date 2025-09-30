# 배열 연산(1)
import numpy as np

# 문제 1
arr = np.array([1, 2, 3, 4])
print("모든 요소에 3을 더한 결과: \n", arr + 3)
print()

# 문제 2
arr = np.array([[5, 10],
                [15, 20]])
print("2차원 배열에서 각 요소를 -1로 곱한 새로운 배열: \n", arr * -1)
print()


# 문제 3
arr1 = np.array([2, 4, 6])
arr2 = np.array([1, 2, 3])
print("두 배열의 요소별 곱셈과 나눗셈 결과: ")
print("곱셈: ", arr1 * arr2)
print("나눗셈: ", arr1 // arr2)
print()

