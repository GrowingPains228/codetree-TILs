n = int(input())
classList = [tuple(map(int, input().split())) for _ in range(n)]

curTime = 0
ans = 0
classList.sort(key=lambda x : (x[1], x[0]))

for (strT, endT) in classList:
    if curTime > strT:
        continue

    curTime = endT
    ans += 1

print(n - ans)