# 배열의 결합과 분리(1)
import numpy as np

# 문제 1
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
row_ab = np.concatenate((a, b), axis=0) 
print("두 배열을 행 방향으로 붙인 결과: \n", row_ab)
print()

# 문제 2 
arr = np.arange(12)
arr_split = np.split(arr, 3)
print(arr_split)

# 문제 3
a = np.array([1, 2])
b = np.array([3, 4])
c = np.array([5, 6])
row_abc = np.stack((a, b, c), axis=0) 
print("shape이 (3, 2)인 배열 생성: \n", row_abc)
print()
print("shape: ", row_abc.shape)