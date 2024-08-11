n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
points = list()
for a, b in lines:
    points.append((a, +1))
    points.append((b, -1))

points.sort()

ans = 0
cnt = 0
for x, v in points:
    cnt += v
    ans = max(ans, cnt)

print(ans)