n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [ [0] * m for _ in range(n) ]
ans = False


def In_Range(x,y):
    return 0 <= x < n and 0 <= y < m


def Can_go(x,y):
    if not In_Range(x,y):
        return False

    if visited[x][y] or grid[x][y] == 0:
        return False

    return True


def dfs(vertex):
    x, y = vertex
    dxs, dys = [1,0],[0,1] # 오른쪽, 아래 방향

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if Can_go(nx, ny):
            visited[nx][ny] = 1
            dfs((nx, ny))


visited[0][0] = 1
dfs((0, 0))
if visited[n-1][m-1]:
    print(1)
else :
    print(0)