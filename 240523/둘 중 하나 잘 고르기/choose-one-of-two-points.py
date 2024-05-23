n = int(input())
cards = [
    tuple(map(int, input().split()))
    for _ in range(2*n)
]

def cmp(card):
    red, blue = card
    return -(red - blue)


cards.sort(key = cmp)

max_sum = 0

# 앞에 n개에서는 빨간색 카드를 선택
max_sum += sum([red for red, _ in cards[:n]])
max_sum += sum([blue for _ , blue in cards[n:]])

print(max_sum)