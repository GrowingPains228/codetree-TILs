OFFSET = 100
MAX_RANGE = OFFSET * 2

N = int(input())

areas = [
    [0 for _ in range(MAX_RANGE)]
    for _ in range(MAX_RANGE)
]

rectangles = [
    tuple(map(int, input().split())) for _ in range(N)
]

for (x1, y1, x2, y2) in rectangles :
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
    for i in range(y1, y2) :
        for j in range(x1, x2) :
            areas[i][j] = 1

area = 0
for row in areas :
    for elem in row :
        if elem > 0 :
            area += 1
print(area)