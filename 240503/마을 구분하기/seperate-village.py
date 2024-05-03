n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [[False]*n for _ in range(n)]
cnt_civil = list()
cnt = 0


def In_range(x,y):
    return 0 <= x < n and 0 <= y < n


def Can_go(x,y):
    if not In_range(x,y):
        return False

    if visited[x][y] or grid[x][y] == 0:
        return False

    return True


def dfs(x,y):
    global cnt
    dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]

    visited[x][y] = True
    cnt += 1
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if Can_go(nx,ny):
            dfs(nx, ny)


def simulation():
    global cnt
    for i in range(n):
        for j in range(n):
            if visited[i][j] or grid[i][j] == 0:
                continue

            cnt = 0
            dfs(i,j)
            cnt_civil.append(cnt)


simulation()
cnt_civil.sort()
print(len(cnt_civil))
for elem in cnt_civil:
    print(elem)