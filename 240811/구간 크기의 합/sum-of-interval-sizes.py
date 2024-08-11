n = int(input())

points = list()
for i in range(n):
    a, b = tuple(map(int, input().split()))
    points.append((a, +1, i))
    points.append((b, -1, i))

points.sort()

ans = 0
segments = set()
pre_num = 0
for x, v, i in points:
    if v == +1:
        if not segments:
            pre_num = x

        segments.add(i)
    else:
        segments.remove(i)
        if not segments:
            ans += x - pre_num

print(ans)