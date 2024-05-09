from collections import deque
#입력 받기
n = int(input())
r1, c1, r2, c2 = map(int, input().split())

# BFS를 위한 함수
step = [[0]*n for _ in range(n)]
visited = [[False]*n for _ in range(n)]
queue = deque()


def in_range(x,y):
    return 0 <= x < n and 0 <= y < n


def can_go(x,y):
    return in_range(x,y) and not visited[x][y]


def push(x,y,s):
    queue.append((x,y))
    visited[x][y] = True
    step[x][y] = s


def bfs():
    dxs, dys = [-2, -2, -1, 1, 2, 2, 1, -1], [-1, 1, 2, 2, 1, -1, -2, -2]

    while queue:
        x,y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)

                if visited[r2-1][c2-1]:
                    break


push(r1-1, c1-1, 0)
bfs()
if visited[r2-1][c2-1]:
    print(step[r2 - 1][c2 - 1])
else:
    print(-1)