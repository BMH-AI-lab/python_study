# print("안녕하세요")

for i in range(5):
    print("안녕하세요")


# range(끝) - 0부터 끝 -1까지 
# range(5) 0. 1, 2, 3, 4, 5


# 구구단 
for i in range(1, 9, 4):
    print(i)

#리스트와 for문
# 리스트
fruits = ['사과', '포도', '오렌지']
for fruit in fruits:
    print(f"과일:{fruit}")

scores = [65, 27, 75, 45]

total = 0
count = 1
for score in scores:
    total += score
    print(f"점수: {score}")
print("total: ", total)


word= "python"
print("========")
for char in word:
    print(char)

for i in range(1, 6):
    for j in range(i):
        print("*", end ='')
    print()

for i in range(5):
    for j in range(i):
        print("*", end ='')
    print()