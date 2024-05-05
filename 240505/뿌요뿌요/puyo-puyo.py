import sys
sys.setrecursionlimit(5000)

# 입력
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
curr_num, cnt = 0, 0
bomb_blocks, max_cnt = 0, 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def can_go(x, y):
    if not in_range(x, y):
        return False

    if visited[x][y] or grid[x][y] != curr_num:
        return False

    return True


def dfs(x, y):
    global curr_num, cnt
    dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]

    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            cnt += 1
            dfs(nx, ny)


def simulation():
    global curr_num, cnt, bomb_blocks, max_cnt
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue

            cnt = 1
            curr_num = grid[i][j]
            dfs(i, j)

            if cnt >= 4:
                bomb_blocks += 1

            max_cnt = max(max_cnt, cnt)


simulation()
print(bomb_blocks, max_cnt)