# NumPy 종합 연습(3)
import numpy as np

# 문제 6
arr = np.arange(35, 75).reshape(10, 4)
print("문제 6. \n", arr)
print()

# 문제 7
arr = np.arange(35, 75).reshape(10, 4)
print("문제 7. \n", arr[::-1, :])
print()

# 문제 8
print("문제 8. \n", arr[1:-1, 2:])