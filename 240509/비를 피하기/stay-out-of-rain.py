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

# 입력된 것 정제 하기
people_group = []
block_rain_group = []
for i in range(n):
    for j in range(n):
        if grid[i][j] in [Element.WALL.value, Element.MOVE_ABLE.value]:
            continue

        if grid[i][j] == Element.PERSON.value:
            people_group.append((i, j))
        else:
            block_rain_group.append((i, j))

# BFS를 위한 변수
queue = deque()
visited = [[False] * n for _ in range(n)]
step = [[0]*n for _ in range(n)]


# 정답 출력을 위한 격자
ans_grid = [[0]*n for _ in range(n)]


def in_range(x,y):
    return 0 <= x < n and 0 <= y < n


def can_go(x, y):
    return (in_range(x, y) and not visited[x][y]
            and (grid[x][y] == Element.MOVE_ABLE.value or grid[x][y] == Element.BLOCK_RAIN.value))


def push(x,y,s):
    visited[x][y] = True
    queue.append((x,y))
    step[x][y] = s


def bfs(ori_x, ori_y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    isArrive = False

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx,ny):
                push(nx, ny, step[x][y] + 1)

                if grid[nx][ny] == Element.BLOCK_RAIN.value:
                    ans_grid[ori_x][ori_y] = step[nx][ny]
                    isArrive = True

    return isArrive

def cal():
    # 초기화
    for x, y in people_group:

        # 초기화
        for i in range(n):
            for j in range(n):
                visited[i][j] = False
                step[i][j] = 0

        push(x, y, 0)
        isArrive = bfs(x,y)

        if not isArrive:
            ans_grid[x][y] = -1


cal()

for row in ans_grid:
    for elem in row:
        print(elem, end = ' ')
    print()