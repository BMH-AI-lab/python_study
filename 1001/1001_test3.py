# 배열 형태 변형, 차원 확장·축소(3)

import numpy as np

# 문제 5
arr = np.array([[[1], [3], [2], [1], [3], [2], [3], [1], [2], [3]]]) # shape (1, 10, 1)
print("shape: ", arr.shape)
arr_squeeze = arr.squeeze()
print("재구성한 shape: ", arr_squeeze.shape)
uniq, inv = np.unique(arr_squeeze, return_inverse = True)
print("고유값 배열: ", inv)

# 문제 6
arr = np.array([ [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]],
                [[3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]] ])  # shape (2, 3, 4)

arr_1d = arr.ravel()
print(arr_1d)
print()
uniq = np.unique(arr_1d)
print("고유값 추출: ", uniq)
print()
uniq_reshaped = uniq.reshape(-1, 1)
print("shape(고유값 개수, 1) 결과: ", uniq_reshaped.shape)
print()
print("shape(고유값 개수, 1)인 2차원 배열: \n", uniq_reshaped)