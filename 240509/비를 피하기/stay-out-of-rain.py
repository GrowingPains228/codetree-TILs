from collections import deque
import enum


class Element(enum.Enum):
    MOVE_ABLE = 0
    WALL = 1
    PERSON = 2
    BLOCK_RAIN = 3


# 입력
n, h, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# BFS를 위한 변수
queue = deque()
visited = [[False] * n for _ in range(n)]
step = [[0]*n for _ in range(n)]

# 정답 출력을 위한 격자
ans_grid = [[0]*n for _ in range(n)]


def in_range(x,y):
    return 0 <= x < n and 0 <= y < n


def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] != Element.WALL.value


def push(x,y,s):
    visited[x][y] = True
    queue.append((x,y))
    step[x][y] = s


def bfs():
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx,ny):
                push(nx, ny, step[x][y] + 1)

                if grid[nx][ny] == Element.PERSON.value:
                    ans_grid[nx][ny] = min(ans_grid[nx][ny], step[nx][ny]) if ans_grid[nx][ny] else step[nx][ny]


# 비를 막아주는 지점에서 출발하는 것!
for i in range(n):
    for j in range(n):
        if grid[i][j] == Element.BLOCK_RAIN.value:
            push(i, j, 0)
bfs()

for i in range(n):
    for j in range(n):
        if grid[i][j] == Element.PERSON.value and ans_grid[i][j] == 0:
            ans_grid[i][j] = -1
        print(ans_grid[i][j], end=" ")
    print()