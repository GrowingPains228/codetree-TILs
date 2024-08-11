n = int(input())
inputs = [tuple(map(int, input().split())) for _ in range(n)]

points = []
for i, (x1, x2) in enumerate(inputs):
    points.append((x1, +1, i))
    points.append((x2, -1, i))

points.sort()
segs = set()

ans = 0
for x, v, i in points:
    if v == +1:
        if not segs:
            ans += 1
        
        segs.add(i)
    else:
        segs.remove(i)

print(ans)