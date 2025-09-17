number1 = [2, 3, 4, 5, 6, 7, 8, 9]
number2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in number1:
    print()
    print(f'[{number}단]')
    for num in number2:
        number3 = number * num
        print(f"{number} x {num} = {number3}" ) 
        
