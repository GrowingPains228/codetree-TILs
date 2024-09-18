USE = True
UNUSE = False
n = int(input())
B_cards = [int(input()) for _ in range(n)]
B_cards.sort()
Cards = [UNUSE] * (2*n+1)

# B에 있는 카드를 체크합니다.
for card in B_cards:
    Cards[card] = USE

ans = 0
j = B_cards[0] + 1
for card in B_cards:
    while j <= 2*n and (Cards[j] == USE or card > j):
        j += 1

    if j > 2*n:
        break

    if Cards[j] == UNUSE:
        ans += 1
        Cards[j] = USE

print(ans)