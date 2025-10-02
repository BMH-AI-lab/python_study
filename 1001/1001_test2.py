# 배열 형태 변형, 차원 확장·축소(2)
import numpy as np

# 문제 3
img= np.random.randint(0, 255, (1, 28, 28, 1))
squeezed1 = np.squeeze(img)
print("squeeze: ", squeezed1.shape)
print()

#문제 4
arr = np.array([[3, 1, 2, 2],
                [1, 2, 3, 1],
                [2, 2, 1, 4]])
flat = arr.flatten()
print("1차원 배열: ", flat)
uniq = np.unique(flat)
print("중복값을 제거: ", uniq)
uniq_reshaped = uniq.reshape(1, -1)
print("shape (1, n)으로 재구성 결과: ", uniq_reshaped)
print("shape (1, n)?: ", uniq_reshaped.shape)
