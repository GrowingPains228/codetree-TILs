myCoins = [2, 5]
cost = int(input())

ans = 0
for coin in myCoins[::-1]:
    ans += cost//coin
    cost %= coin

print(ans if cost == 0 else -1)