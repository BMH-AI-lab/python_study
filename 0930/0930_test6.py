# NumPy 종합 연습(4)
from numpy.random import default_rng
import numpy as np

# 문제 9
rng = default_rng(seed = 42)

arr = np.random.randint(1, 51, (5, 6))
print("문제 9")
print("짝수만 :", arr[arr % 2 == 0])
print()

# 문제 10
arr = np.arange(0, 100).reshape(10, 10)
rows = [1, 3, 5]
cols = [2, 4, 6]

print("문제 10.")
print("선택된 원소들: \n", arr[rows][:, cols])
print()


# 문제 11
arr = rng.integers(0, 10, size=15)
arr2 = arr[::2]
print("문제 11.")
print("짝수 인덱스 값들:", arr2)
arr3 = arr[arr >= 5]
print("짝수 인덱스 중 5 이상인 값들:", arr3)