OFFSET = 100
MAX_RANGE = OFFSET * 2 + 1
n = int(input())
area = [
    [0]* MAX_RANGE
    for _ in range(MAX_RANGE)
]

# color = 1 : 레드, 2 : 블루
def Set_color(rect, color) :
    x1, y1, x2, y2 = rect
    x1, y1, x2, y2 = x1 + OFFSET , y1 + OFFSET , x2 + OFFSET , y2 + OFFSET 
    for i in range(y1, y2) :
        for j in range(x1, x2) :
            area[i][j] = color

for i in range(n) :
    color_type = 1 if i%2 == 0 else 2
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    Set_color((x1, y1, x2, y2), color_type)
    
cnt_blue = 0
for row in area :
    for elem in row :
        if elem == 2:
            cnt_blue += 1

print(cnt_blue)