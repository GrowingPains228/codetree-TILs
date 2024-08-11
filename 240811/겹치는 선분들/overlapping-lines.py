from collections import deque
n, k = map(int, input().split())
lines = [tuple(input().split()) for _ in range(n)]

startPos = 0
points = list()

def drawLine(value, direction):
    global startPos
    if direction == 'R':
        points.append((startPos, +1))
        points.append((startPos + value, -1))
        startPos += value
    else:
        points.append((startPos - value, +1))
        points.append((startPos, -1))
        startPos -= value

for (v, d) in lines:
    drawLine(int(v), d)

points.sort()
ans = 0
sum_result = 0
for i, (x, v) in enumerate(points):
    if sum_result >= k:
        prev_x, _ = points[i-1]
        ans += x - prev_x
    
    sum_result += v

print(ans)