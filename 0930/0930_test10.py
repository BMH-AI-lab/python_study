import numpy as np

# 문제 4
arr = np.array([[10, 20],
                [30, 40],
                [50, 60]])

print("행별 평균: ", np.mean(arr, axis=1))
print("열별 평균: ", np.mean(arr, axis=0))
print()

# 문제 5
arr = np.array([2, 4, 4, 4, 5, 5, 7, 9])
mean = np.mean(arr)
std = np.std(arr)
deviation = arr - mean
print("편차 배열:", deviation)

# 문제 6
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("2차원 배열 행 단위 누적 합과 열 단위 누적 곱:")
print("행 단위 누적 합: \n", np.cumsum(arr, axis=1))
print("열 단위 누적 곱: \n", np.cumprod(arr, axis=0))