card = [5, 3, 7]
card.extend([4, 9])
print('2장의 카드 추가한 결과: ', card)
print('카드의 가장 큰 수: ', max(card))
print('카드의 가장 작은 수:', min(card))
print('카드의 총합: ', sum(card))
card.sort()
card.pop(4)
print('카드 정렬 후 마지막 숫자제거(최종 리스트): ', card)


