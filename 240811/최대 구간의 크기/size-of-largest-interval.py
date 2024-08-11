n = int(input())

points = list()

for i in range(n):
    a,b = tuple(map(int, input().split()))
    points.append((a, +1, i))
    points.append((b, -1, i))

points.sort()

segments = set()
ans = 0
start_dot = 0
for x, v, i in points:
    if v == +1:
        if not segments:
            start_dot = x
        
        segments.add(i)
    else:
        segments.remove(i)
        if not segments:
            ans = max(ans, x - start_dot)

print(ans)