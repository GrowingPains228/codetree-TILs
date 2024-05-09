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
    if not in_range(x, y) or visited[x][y]:
        return False

    if grid[x][y] == Element.WALL.value:
        return False

    return True


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


def cal():
    # 초기화
    for x, y in people_group:

        # 초기화
        for i in range(n):
            for j in range(n):
                visited[i][j] = False
                step[i][j] = 0

        push(x, y, 0)
        bfs()

        is_Arrive = False
        for (v_x, v_y) in block_rain_group:
            if visited[v_x][v_y] :
                ans_grid[x][y] = min(ans_grid[x][y], step[v_x][v_y]) if ans_grid[x][y] != 0 else step[v_x][v_y]
                is_Arrive = True

        if not is_Arrive:
            ans_grid[x][y] = -1


cal()

for row in ans_grid:
    for elem in row:
        print(elem, end = ' ')
    print()