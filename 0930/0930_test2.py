# 인덱싱과 슬라이싱(3)
import numpy as np

arr = np.array([[10, 20, 30], [55, 65, 75], [40, 45, 50], [70, 80, 90], [15, 25, 35]])
print("문제 8: \n", arr[arr > 50][:6].reshape(2, 3))
print()

arr = np.arange(1, 17).reshape(4, 4)
print("문제 9: ", arr[[0, 1, 2, 3], [1, 3, 0, 2]])
print()

arr3d = np.arange(24).reshape(2, 3, 4)
print("문제 10: \n", arr3d[:, :, 1]) 