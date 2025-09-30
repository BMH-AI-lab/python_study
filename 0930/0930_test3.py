# NumPy 종합 연습(1)

import numpy as np
from numpy.random import default_rng

# 문제 1
arr = np.arange(25).reshape(5, 5)
print("문제 1.")
print("가운데 행: ", arr[2])
print("가운데 열: ", arr[[0, 1, 2, 3, 4], [2, 2, 2, 2, 2]])
print()

# 문제 2
rng = default_rng(seed = 42)

arr = np.random.randint(0, 100, (10, 10))
print("문제 2.")
print("짝수 인덱스 행: \n", arr[::2])
print()

# 문제 3
arr = np.arange(50).reshape(5, 10)
print("문제 3.")
print("부분 배열: \n", arr[1:4, 2:8])