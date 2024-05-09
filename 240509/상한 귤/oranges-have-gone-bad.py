from collections import deque
#입력
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
old_oranges = [(i,j) for i in range(n)
               for j in range(n)
               if grid[i][j] == 2]


# bfs를 위한 변수
visited = [[False]*n for _ in range(n)]
step = [[0]*n for _ in range(n)]
queue = deque()


def in_range(x,y):
    return 0 <= x < n and 0 <= y < n


def can_go(x,y):
    return in_range(x,y) and grid[x][y] == 1 and not visited[x][y]


def push(x,y,s):
    visited[x][y] = True
    step[x][y] = s
    queue.append((x,y))


def bfs():
    dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)


for vertex in old_oranges:
    x, y = vertex
    push(x, y, 0)
bfs()

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            print(-1, end = " ")
        elif grid[i][j] == 1 and not visited[i][j]:
            print(-2, end=" ")
        else:
            print(step[i][j], end = " ")
    print()