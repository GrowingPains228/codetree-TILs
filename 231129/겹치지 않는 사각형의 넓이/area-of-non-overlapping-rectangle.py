OFFSET = 1000
MAX_RANGE = OFFSET * 2 
# A,B 직사각형을 덮는 최대 넓이를 구한 다음
# M 사각형
area = [
    [0 for _ in range(MAX_RANGE + 1)]
    for _ in range(MAX_RANGE + 1)
]

# tf == True : 색칠하기
# tf == False : 색지우기
def color_area(rectangle, tf = True) :
    if tf :
        x1, y1, x2, y2 = rectangle
        x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
        for i in range(y1, y2) :
            for j in range(x1, x2) :
                area[i][j] = 1
    else :
        x1, y1, x2, y2 = rectangle
        x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
        for i in range(y1, y2) :
            for j in range(x1, x2) :
                area[i][j] = 0

A = tuple(map(int, input().split()))
B  = tuple(map(int, input().split()))
M = tuple(map(int, input().split()))

color_area(A)
color_area(B)
color_area(M, False)

cnt = 0
for row in area :
    for elem in row :
        if elem > 0 :
            cnt += 1
print(cnt)