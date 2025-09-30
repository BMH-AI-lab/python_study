import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print("=== 1차원 배열===")
print("shape: ", arr_1d.shape)
print("ndim", arr_1d.ndim)
print(arr_1d.reshape(4, -1))
print("size", arr_1d.size)
print()
print("=== 2차원 배열===")
print("shape: ", arr_2d.shape)
print("ndim", arr_2d.ndim)
print("size", arr_2d.size)

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])


print("배열 a:", a)
print("배열 b:", b)


print("덧셈 (a + b): ", a + b)
print("뺼셈 (a - b): ", a - b)
print("곱셈 (a * b): ", a * b)
print("거듭제곱 (a ** b):", a**b)
print("나눗셈 (a / b): ", a / b)
print("몫 (a // b): ", a // b)
print("나머지 (a % b): ", a % b)