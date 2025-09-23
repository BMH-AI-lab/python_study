def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return 0
    return a / b

import calculator

result = calculator.add(5, 0)
print(result)

import math 
import random 
import datetime 

print(math.pi)
print(random.randint(1, 11))
print(datetime.datetime.now())