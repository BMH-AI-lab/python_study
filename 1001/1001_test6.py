# 배열의 정렬(1)
import numpy as np

# 문제 1
arr = np.array([7, 2, 9, 4, 5])
print("오름차 순 배열: ", np.sort(arr))
print("내림차 순 배열: ", np.sort(arr)[::-1])
print()

# 문제 2
arr = np.array([[9, 2, 5],
                [3, 8, 1]])
print("각 행(row) 별로 오름차순 정렬된 배열: \n", np.sort(arr,  axis=1))
print()

# 문제 3
arr = np.array([10, 3, 7, 1, 9])
argsort_arr = np.argsort(arr)
print("정렬 결과(오름차순)가 되는 인덱스 배열: \n", argsort_arr)
print("원본 배열을 직접 재정렬한 결과: \n", arr[argsort_arr])
print()

# 문제 4
arr = np.array([[4, 7, 2],
                [9, 1, 5],
                [6, 8, 3]])
print("열(column) 기준(axis=0)으로 오름차순 정렬된 배열: \n", np.sort(arr, axis=0))
print()