OFFSET = 1000
MAX_RANGE = OFFSET * 2 + 1

area = [
    [0] * MAX_RANGE
    for _ in range(MAX_RANGE)
]

def color_area(rect, tf = True) :
    x1, y1, x2, y2 = rect
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
    if tf : 
        for i in range(y1, y2) :
            for j in range(x1, x2) :
                area[i][j] = 1
    else :
        for i in range(y1, y2) :
            for j in range(x1, x2) :
                area[i][j] = 0

rect1 = tuple(map(int, input().split()))
rect2 = tuple(map(int, input().split()))

# 최종으로 남은 넓이만큼 색칠되어 있음.
color_area(rect1)
color_area(rect2,False)

#여기서 색칠된 부분을 덮을 최소 직사각형 넓이를 구해야함.

x1, y1, x2, y2 = rect1
x1, y1, x2, y2 = x1+OFFSET, y1+OFFSET, x2+OFFSET, y2+OFFSET
max_x1, max_y1 = (0,0)

for i in range(y2, y1 -1, -1) :
    for j in range(x2 , x1 - 1, -1) :
        if area[i][j] == 1:
            if max_x1 < j :
                max_x1 = j + 1
            if max_y1 < i :
                max_y1 = i + 1
                
min_x1, min_y1 = MAX_RANGE, MAX_RANGE
for i in range(y1, y2) :
    for j in range(x1, x2) :
        if area[i][j] == 1:
            if min_x1 >= j :
                min_x1 = j
            if min_y1 >= i :
                min_y1 = i

if (min_x1 == MAX_RANGE) and (min_y1 == MAX_RANGE) :
    min_x1, min_y1 = (0,0)

print((max_x1 - min_x1) * (max_y1-min_y1))