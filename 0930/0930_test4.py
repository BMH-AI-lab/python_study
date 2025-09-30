# NumPy 종합 연습(2)
from numpy.random import default_rng
import numpy as np

# 문제 4
rng = np.random.default_rng(seed=42)
arr = rng.integers(0, 10, size=(4, 4), dtype=np.int32)

main_diag = [arr[i, i] for i in range(4)]
anti_diag = [arr[i, 3 - i] for i in range(4)]

print("문제 4.")
print("주대각선:", repr(main_diag))
print("부대각선:", repr(anti_diag))
print()

# 문제 5
arr = np.random.randint(0, 9, (3, 4, 5))
print("문제 5.")
print("두 번째 층의 첫 행 마지막 열 값: ", arr[1, 0, -1])

