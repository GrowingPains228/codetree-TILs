n = int(input())
# 2차원 숫자 배열
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
# 방향 2차원 배열
dir_grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
# 시간 위치
start_pos = tuple(map(int, input().split()))
ans = 0
cnt = 0
def In_Range(x,y):
    return 0 <= x < n and 0 <= y < n


# 해당 방향에 이동할 블럭이 있는지 체크.
def Is_Move(x,y):
    dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
    movable_arr = []
    my_value = grid[x][y]
    dir = dir_grid[x][y] - 1
    nx, ny = x + dxs[dir], y + dys[dir]
    while In_Range(nx,ny):
        if my_value < grid[nx][ny]:
            movable_arr.append((nx,ny))
        nx, ny = nx + dxs[dir], ny + dys[dir]

    return movable_arr[:]


#
def choose(x,y):
    global ans, cnt
    next_move_arr = Is_Move(x,y)

    if len(next_move_arr) == 0:
        ans = max(ans, cnt)
        return

    for next_x, next_y in next_move_arr:
        cnt += 1
        choose(next_x, next_y)
        cnt -= 1


x,y = start_pos
choose(x - 1, y -1)
print(ans)