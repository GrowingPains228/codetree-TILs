import sys
target = int(input())
coinList = [5,2]
ans = 0

def is_impossible(num):
    return num < 5 and num % 2 != 0


if is_impossible(target):
    print(-1)
    sys.exit()


for coin in coinList:
    if is_impossible(target%coin):
        ans += target//coin - 1
        target = target%coin + coin
    else:
        ans += target//coin
        target %= coin

print(ans)