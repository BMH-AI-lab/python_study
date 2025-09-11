second = int(input(""))
if second >= 3600:
    print(f'{second // 3600}시',  end= ' ')

second %= 3600

if second >= 60:
    print(f'{second // 60} 분', end= ' ')

second %= 60

print(f'{second} 초')