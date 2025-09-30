# 인덱싱과 슬라이싱(1~2)
import numpy as np

arr = np.arange(10, 30, 2)
print("문제 1: ", arr[[1, 3, 5]])
print()

arr = np.arange(1, 10).reshape(3, 3)
print("문제 2: ", arr[[0, 1, 2], [0, 1, 2]])
print()

arr = np.arange(1, 13).reshape(3, 4)
arr[:, -1] = -1
print("문제 3: \n", arr)
print()

arr = np.arange(1, 17).reshape(4, 4)
print("문제 4 - 행 역순: \n", arr[::-1, :])
print()
print("문제 4 - 열 역순: \n", arr[:, ::-1])
print()

arr = np.arange(1, 21).reshape(4, 5)
copy_arr = arr[1:3, 1:4].copy()
print("문제 5 - 부분 배열:\n", copy_arr)
print()

arr = np.array([[ 4, 9, 12, 7], [10, 15, 18, 3], [ 2, 14, 6, 20]])
print("문제 6: ", arr[(arr >= 10) & (arr % 2 == 0)])
print()

arr = np.arange(1, 26).reshape(5, 5)
print("문제 7: \n", arr[[1, 3], :][:, [4, 0, 2]])