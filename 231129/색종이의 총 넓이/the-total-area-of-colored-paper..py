OFFSET = 100
MAX_RANGE = 200
length = 8

area = [
    [0] * (MAX_RANGE + 1)
    for _ in range(MAX_RANGE + 1)
]

def color_range(dot) :
    (x1,y1) = dot
    x1 += OFFSET
    y1 += OFFSET
    for i in range(y1, y1 + 8) :
        for j in range(x1, x1+8) :
            area[i][j] = 1

n = int(input())


segment = []
for _ in range(n) :
    dot = (x1, y1) = tuple(map(int,input().split()))
    color_range(dot)

cnt = 0
for row in area :
    for elem in row :
        if elem > 0 :
            cnt += 1

print(cnt)