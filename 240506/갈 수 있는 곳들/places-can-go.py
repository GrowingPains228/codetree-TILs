from collections import deque

n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [[False] * n for _ in range(n)]
queue = deque()
ans_cnt = 0

# 시작 지점 입력 받기
for _ in range(m):
    (x,y) = tuple(map(int, input().split()))
    x,y = x - 1, y - 1
    visited[x][y] = True
    ans_cnt += 1
    queue.append((x, y))


def in_range(x,y):
    return 0 <= x < n and 0 <= y < n


def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and grid[x][y] != 1


def bfs():
    global ans_cnt
    dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]

    while queue:
        curr_vertex = queue.popleft()
        (x, y) = curr_vertex
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                ans_cnt += 1
                visited[nx][ny] = True
                queue.append((nx, ny))


bfs()
print(ans_cnt)