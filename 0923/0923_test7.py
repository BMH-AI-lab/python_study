from datetime import date

birthday_input = input("생일을 입력하세요: ")

birth_year, birth_month, birth_day = map(int, birthday_input.split('-'))

today = date.today()

my_birthday = date(today.year, birth_month, birth_day)

if my_birthday >= today:
    my_day = (my_birthday - today).days

else:
    next_bitrhday = date(today.year + 1, birth_month, birth_day)
    my_birth = (next_bitrhday - today).days 

print(f"생일까지 남은 일수: {my_birth}일")