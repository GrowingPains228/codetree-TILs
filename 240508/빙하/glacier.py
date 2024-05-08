from collections import deque
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [[False] * m for _ in range(n)]
ans = 0
Ice_arr = list()
bfs_queue = deque()
ans_time = 0
ans_Ice = 0

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
    if not in_range(x,y):
        return False

    if visited[x][y]:
        return False

    if grid[x][y] == 1:
        Ice_arr.append((x,y))
        visited[x][y] = True
        return False

    return True


def bfs():
    dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]
    while bfs_queue:
        x,y = bfs_queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx,ny):
                visited[nx][ny] = True
                bfs_queue.append((nx, ny))


def Melt():
    global ans_Ice
    ans_Ice = len(Ice_arr)
    while Ice_arr:
        x,y = Ice_arr.pop()
        grid[x][y] = 0


def simulate():
    global ans_time

    while True:
        initialize()
        bfs()
        if len(Ice_arr) > 0:
            ans_time += 1
            Melt()
        else:
            break


simulate()
print(ans_time, ans_Ice)