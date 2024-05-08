from collections import deque
import enum


class Element(enum.Enum):
    WATER = 0
    GLACIER = 1


n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [[False] * m for _ in range(n)]
Ice_arr = deque()
bfs_queue = deque()
elapsed_time = 0
last_melt_cnt = 0


# bfs 를 통해 빙하를 판별할때,
# 접근하려고 했지만 접근하지 못한 vertex에 대해 기억해 뒀다가,
# 해당 vertex는 빙하이므로, 다음 시퀀스에 녹인다.
# bfs를 다 돌고, 모든 vertex가 물일때,
# simulation 종료 및 '총 시간'과 '마지막에 녹여진 빙하 갯 수' 출력
def in_range(x,y):
    return 0 <= x < n and 0 <= y < m


def initialize():
    global Ice_arr, bfs_queue
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

    Ice_arr = list()

    bfs_queue.append((0,0))
    visited[0][0] = True


def can_go(x, y):
    return in_range(x,y) and grid[x][y] == Element.WATER.value and not visited[x][y]


# 범위를 벗어나지 않으면서 빙하여야 하고 이미
# 선택된 적이 없어야 중복 없이 녹아야할 빙하 목록에
# 해당 빙하를 문제 없이 추가할 수 있다.
def is_glacier(x,y):
    return in_range(x,y) and grid[x][y] == Element.GLACIER.value and not visited[x][y]


def bfs():
    dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]
    while bfs_queue:
        x,y = bfs_queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx,ny):
                visited[nx][ny] = True
                bfs_queue.append((nx, ny))
            elif is_glacier(nx,ny):
                Ice_arr.append((nx,ny))
                visited[nx][ny] = True


def Melt():
    while Ice_arr:
        x,y = Ice_arr.popleft()
        grid[x][y] = Element.WATER.value


def simulate():
    global elapsed_time, last_melt_cnt, bfs_queue

    bfs()

    # 녹일 빙하가 없다면 종료
    if not Ice_arr:
        return False

    elapsed_time += 1
    last_melt_cnt = len(Ice_arr)

    bfs_queue = Ice_arr.copy()

    # 녹아야 할 빙하들을 녹여준다.
    Melt()

    return True


bfs_queue.append((0,0))
visited[0][0] = True

while True:
    is_glacier_exist = simulate()

    if not is_glacier_exist:
        break

print(elapsed_time, last_melt_cnt)