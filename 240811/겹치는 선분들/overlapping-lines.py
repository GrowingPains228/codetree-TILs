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

sum_result = 0
stQueue, endPos = deque(), deque()
for x, v in points: 
    if sum_result >= k and sum_result + v < k:
        endPos.append(x)
    elif sum_result < k and sum_result + v >= k:
        stQueue.append(x)
    
    sum_result += v

ans_length = 0
for st_x, end_x in zip(stQueue, endPos):
    ans_length += end_x - st_x

print(ans_length)