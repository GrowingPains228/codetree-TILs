from collections import deque
# 입력
n,m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

#시작점과 끝점은 문제에 주어졌다.
START_POS = (0,0)
END_POS = (n-1, m-1)

# BFS 탐색을 위한 변수들
q = deque()
visited = [
    [False] * m for _ in range(n)
]

step = [
    [0] * m for _ in range(n)
]


def in_range(x,y):
    return 0 <= x < n and 0 <= y < m


def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and grid[x][y] == 1


def push(x,y,s):
    visited[x][y] = True
    step[x][y] = s
    q.append((x,y))


def bfs():
    dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]

    while q :
        x,y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)


push(0, 0, 0)
bfs()
if visited[n-1][m-1]:
    print(step[n-1][m-1])
else:
    print(-1)