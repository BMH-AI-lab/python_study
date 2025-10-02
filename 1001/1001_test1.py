# 배열 형태 변형, 차원 확장·축소(1)
import numpy as np

# 문제 1
arr = np.array([[10, 20], [30, 40], [50, 60]])
rav1 = arr.ravel()
flat1 = arr.flatten()
print("원본: \n", arr)
print("ravel: ", rav1)
print("flatten: ", flat1)
print()
arr[0, 0] = 999
print("<arr의 첫 번째 원소(arr[0,0])를 999로 바꾼 결과>\n", arr)
rav2 = rav1.ravel()
flat2 = flat1.flatten()
print("999로 바꾼 뒤 ravel 결과: ", rav2)
print("999로 바꾼 뒤 flatten 결과: ", flat2)
print()

# 문제 2
img= np.random.rand(32, 32)
img_extended = np.expand_dims(img, axis=0)
print("expand_dims를 사용하여 shape 바꾼 결과: ", img_extended.shape)
print()

