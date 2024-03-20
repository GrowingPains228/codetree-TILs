n, r, c = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
max_num = 0
cur_x, cur_y = (r-1, c-1)


def In_range(x,y) :
    return x >= 0 and y >= 0 and x < n and y < n


def simulation():
    global cur_x, cur_y
    dxs, dys = [-1, 1, 0 ,0], [0, 0, -1, 1]
    print(grid[cur_x][cur_y], end = " ")
    while True:
        max_num = 0
        max_x, max_y = (-1, -1)
        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy
            if In_range(nx, ny) and grid[cur_x][cur_y] < grid[nx][ny]  :
                max_x, max_y = nx, ny
                max_num = grid[nx][ny]
                break

        if not max_num :
            break
        
        print(max_num, end = " ")
        cur_x, cur_y = nx, ny

simulation()