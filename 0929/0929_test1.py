import numpy as np
from numpy.random import default_rng

# 문제 1
zero_1 = np.full((3, 4), 0)
print("문제 1 과정: \n", zero_1)
print()
zero_2 = np.full(zero_1.shape, 5)
print("문제 1: \n", zero_2)
print()

# 문제 2
print("문제 2: \n", np.arange(0, 22, 2))
print()

# 문제 3
rng = default_rng(seed = 42)
print("문제 3: \n", rng.random((2, 3)))
print()

# 문제 4  
number1 = rng.normal(100, 20, size = 6)
print("문제 4: \n", number1)
print()

# 문제 5 
number2 = np.arange(1, 21)
print("문제 5 과정: ", number2)
print()

print("문제 5:\n", number2.reshape(4, 5))
print()

# 문제 6
number3 = np.linspace(0, 1, 12).reshape(3, 4)
print("문제 6: \n", number3)
print()

# 문제 7
number4 = np.random.randint(0, 100, (10, 10))
a = np.eye(10, dtype = int)
result = number4 + a
print("문제 7과정: \n")
print(number4)
print()
print(a)
print()
print("문제 7: \n", result)
print()

# 문제 8
number5 = np.random.randint(0, 10, (2, 3, 4))
print("문제 8: \n", number5)