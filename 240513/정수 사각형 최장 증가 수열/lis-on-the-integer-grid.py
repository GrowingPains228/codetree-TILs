n = int(input())
NOTUSED = 500      # 시간복잡도가 O(N^3)을 넘으면 안된다!
grid = [list(map(int, input().split()))
        for _ in range(n)]
memo =[[NOTUSED]*n for _ in range(n)]


def in_range(x,y):
    return 0 <= x < n and 0 <= y < n


def can_go(x,y, value):
    return in_range(x,y) and grid[x][y] > value


def find_path(x,y):
    if memo[x][y] != NOTUSED:
        return memo[x][y]

    max_path = 1
    dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, grid[x][y]) :
            max_path = max(max_path, find_path(nx, ny) + 1)

    memo[x][y] = max_path
    return max_path


for i in range(n):
    for j in range(n):
        find_path(i, j)

print(max(max(row for row in memo)))