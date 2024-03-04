n,m,q = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
avg_grid = [[0]*m for _ in range(n)]

def in_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < m

# 경계에 있는 직사각형 회전
def spin_around(x1, y1, x2, y2):
    #첫번째 회전 : x1 줄, 오른쪽 방향
    temp1 = grid[x1][y2]
    for j in range(y2, y1, -1):
        grid[x1][j] = grid[x1][j-1]
    
    # 두번째 회전 : y2 줄, 아래 방향
    temp2 = grid[x2][y2]
    for i in range(x2, x1, -1):
        grid[i][y2] = grid[i-1][y2]
    grid[x1+1][y2] = temp1

    # 세번째 회전 : x2줄, 왼쪽 방향
    temp1 = grid[x2][y1]
    for j in range(y1, y2) :
        grid[x2][j] = grid[x2][j+1]
    grid[x2][y2-1] = temp2

    #네번째 회전 : y1줄, 위 방향
    for i in range(x1, x2) :
        grid[i][y1] = grid[i+1][y1]
    grid[x2-1][y1] = temp1

# 평균 구하는 함수
def cal_avgAround(x1, y1, x2, y2):
    global avg_grid
    range_x = [-1, 0, 0, 1]
    range_y = [0, -1, 1, 0]
    avg_grid = [[0]*m for _ in range(n)]

    for x in range(x1, x2+1) :
        for y in range(y1, y2+1) :
            # x,y 는 더해준 초기값
            cnt = 1            
            value = grid[x][y]

            for dx, dy in zip(range_x, range_y):
                if in_range(x + dx, y + dy):
                    cnt += 1
                    value += grid[x + dx][y + dy]

            avg_grid[x][y] = value//cnt

# 값 복사
def Reflect(x1, y1, x2, y2) :
    global avg_grid
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            grid[i][j] = avg_grid[i][j]

# 바람 불어준 횟수만큼 반복
for _ in range(q) :
    r1, c1, r2, c2 = tuple(map(int, input().split()))
    spin_around(r1-1, c1-1, r2-1, c2-1)
    cal_avgAround(r1-1, c1-1, r2-1, c2-1)
    Reflect(r1-1, c1-1, r2-1, c2-1)

for row in grid:
    for elem in row :
        print(elem, end = ' ')
    print()