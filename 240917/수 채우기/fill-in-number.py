MAX_NUM = 10**6

n = int(input())
ans = MAX_NUM

for i in range(0, MAX_NUM + 1):
    remainder = n - i*5
    if remainder >= 0 and remainder % 2 == 0:
        ans = min(ans, i + remainder//2)

print(ans if ans != MAX_NUM else -1)