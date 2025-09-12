bus = ["철수", "영희"]
bus.extend(["민수", "지훈"])
print('철수, 영희, 민수, 지훈 탑승 후 결과:', bus)

bus.pop(1)
print('영희 하차 후 결과: ', bus)
bus.insert(1, "수진")
print('수진 탑승 후 결과', bus)

bus.pop(2)
print('민수 하차 후 결과: ', bus)
bus.reverse()
print('순서가 뒤집힌 결과: ', bus)