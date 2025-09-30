# 통계 함수 및 집계 연산
import numpy as np

# 문제 1
arr = np.array([5, 10, 15, 20])

print("배열의 전체 합계: ", np.sum(arr))
print("배열의 전체 평균: ", np.mean(arr))

# 문제 2
arr = np.array([[3, 7, 1],
                [9, 2, 8]])
print("배열의 최소값: ", np.min(arr))
print("배열의 최소값: ", np.max(arr))


# 문제 3
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("각 열의 합계: ", np.sum(arr, axis=0))
print("각 행의 합계: ", np.sum(arr, axis=1))

