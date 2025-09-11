year, month, day = input("년, 월, 일을 입력해주세요: ").split('.')
c, d, e = input("시, 분, 초를 입력해주세요: ").split(':')

year = int(year)
month = int(month)
day = int(day)
c = int(c)
d = int(d)
e = int(e)

print("RE3의 개강일은", year, "년", month, "월", day, "일")
print("시작 시간은", c, "시", d, "분", e, "초 입니다.")