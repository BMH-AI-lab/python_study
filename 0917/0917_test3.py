# 문제1. 제곱값 리스트 만들기
squares = [x ** 2 for x in range(1, 11)]
print("1부터 10까지의 제곱값 리스트: ", squares)

# 문제 2. 3의 배수만 리스트로 만들기
number = [x for x in range(1, 51) if x % 3 == 0]
print("1부터 50까지의 수 중에서 3의 배수 리스트: ", number)

# 문제 3. 문자열 리스트에서 길이가 5 이상인 단어만 뽑기
fruits = ["apple", "fig", "banana", "plum", "cherry", "pear", "orange"]
String_fruits = [String_fruits for String_fruits in fruits if len(String_fruits) >= 5]
print("길이가 5 이상인 단어: ", String_fruits)