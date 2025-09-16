# 문제1. 리스트의 값을 두 배로 변환하기
numbers = [3, 6, 1, 8, 4]
number2 = []

for i in range(0, 5):
    number2.append(numbers[i] * 2)
print(number2)

# 문제2. 문자열의 길이 구해서 새 리스트 만들기
words = ["apple", "banana", "kiwi", "grape"]
word2 = []
for i in words:
    word2.append(len(i))
print(word2)

# 문제3. 좌표 튜플에서 x, y 좌표 나누기
x_values = []
y_values = []
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
for x, y in coordinates:
    x_values.append(x)
    y_values.append(y)
print("x값: ", x_values)
print("y값: ", y_values)

        