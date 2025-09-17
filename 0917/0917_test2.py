n = int(input("몇 줄? >"))
print()
print("왼쪽정렬")
for i in range(1, n + 1):
    print('*' * i)
print()
n = int(input("몇 줄? >"))
print()
print("가운데정렬")
for i in range(1, n + 1):
    print(' ' * (n - i), '*' * (2 * i - 1))
print()
n = int(input("몇 줄? >"))
print()
print("오른쪽정렬")
for i in range(1, n + 1):
    print(' ' * (n - i), '*' * (i))

