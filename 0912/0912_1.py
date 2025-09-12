list1 = list()
list2 = list("Hello")

print(list1)
print(list2)

print('인덱스 0: ', list2[0])
print('인덱스 3: ', list2[3])
print('인덱스 4: ', list2[4])

print('인덱스 -1: ', list2[-1])
print('인덱스 -3: ', list2[-3])

list2[4] = 'a'
print('list2', list2)

# text = 'python'
# text[1] = 'a'
# print('text'. text)


# list3 = list('python')
text3 = 'Hello'
#  H  e  l  l  o
#  0  1  2  3  4
# -5 -4 -3 -2 -1
#print('list3[:]', list3[:])
print('text3[:]', text3[:])
print('text3[:-3]', text3[:3])
print('text3[2:4]', text3[2:4])
print('text3[-3:-1]', text3[-3:-1])

print('text3[::-1]', text3[::-1])
print('text3[::-2]', text3[::-2])
print('text3[:-4:-2]', text3[:-4:-2])

numbers = [10, 20, 30, 40]
print('numbers[1:3]', numbers[1:3])
print('numbers[:3:2]', numbers[:3:2])
print('numbers 뒤집기: ', numbers[::-1])