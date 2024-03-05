n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
r,c,m1,m2,m3,m4,direction = tuple(map(int, input().split()))

# 반시계 방향(0) 밀어내기 회전 => 시계 방향으로 당겨오는 회전
# 시게 방향(1) 밀어내기 회전 => 반시계 방향으로 당겨오는 회전
dir_x = [-1, -1, 1, 1]
dir_y = [-1, 1, 1, -1]

def move_func(x,y,m1,m2,m3,m4,direction):
    temp = grid[x][y]
    order_range = [m4, m3, m2, m1] if direction == 0 else [m1, m2, m3, m4]

    for (dx, dy), m in zip(zip(dir_x, dir_y), order_range):
        if direction == 1:
            dy *= -1

        # m 만큼 이동 시작
        for _ in range(m) :
            nx, ny = x + dx, y + dy
            grid[x][y] = grid[nx][ny]
            x,y = nx, ny
    
    fx, fy = x - 1, y + (1 if direction == 0 else -1)
    grid[fx][fy] = temp


move_func(r-1,c-1,m1,m2,m3,m4,direction)

for row in grid :
    for elem in row:
        print(elem, end = ' ')
    print()