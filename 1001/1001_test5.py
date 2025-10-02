# 배열의 결합과 분리(2)
import numpy as np

# 문제 4
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
arr_cont = np.concatenate((a, b))
arr_stack = np.stack((a, b), axis=2)
print("shape (2, 2, 3)인 3차원 배열: \n", arr_stack)
print()
print("shape:", arr_stack.shape)
print()

# 문제 5
arr = np.arange(8)
arr_split = np.split(arr, [2, 5])
print(" 2:3:3 비율(총 3개)로 분할 결과: ", arr_split)

# 문제 6
a = np.ones((2, 3))
b = np.zeros((2, 3))

one_stack = np.stack((a, b), axis=0)
two_stack = np.stack((a, b), axis=1)
print("axis=0 stack: \n", one_stack)
print("axis=0 stack의 shape: ",one_stack.shape)
print()
print("axis=1 stack: \n",two_stack)
print("axis=1 stack의 shape: ", two_stack.shape)
