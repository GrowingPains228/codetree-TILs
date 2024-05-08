from collections import deque

# 입력 받기
# n : 격자 크기
# k : 도시의 수
# u,d : 상,하,좌,우로 이동할 수 있는 도시 간의 높이차 (u 이상 d이하)
n, k, u, d = map(int, input().split())

# 격자 정보
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# BFS를 위한 방문 격자 및 큐
bfs_queue = deque()
visited = [[False] * n for _ in range(n)]

# 최종 출력할 도시 수 변수
ans_cnt = 0

# BFS 내부에서 사용할 cnt 변수
cnt_in_bfs = 0

# 방향 정의 리스트
dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]

# Backtracking 내부에서 선택한 좌표 리스트
selected_group = list()

# Backtracking 내부에서 방문한 좌표 리스트
backtracking_grid = [
    (i, j) for j in range(n)
    for i in range(n)
]
visited_Backtracking = [[False] * (n*n)]


def in_range(x,y):
    return 0 <= x < n and 0 <= y < n


def can_go(x, y, target_value):
    return in_range(x,y) and not visited[x][y] and u <= abs(grid[x][y] - target_value) <= d


def initialize():
    global cnt_in_bfs
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    cnt_in_bfs = 0


def bfs():
    global cnt_in_bfs

    initialize()

    for elem in selected_group:
        x, y = elem
        bfs_queue.append((x, y))
        visited[x][y] = True
        cnt_in_bfs += 1

    while bfs_queue:
        x, y = bfs_queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, grid[x][y]):
                visited[nx][ny] = True
                cnt_in_bfs += 1
                bfs_queue.append((nx, ny))


def selected_city(curr_cnt, curr_idx):
    global ans_cnt, cnt_in_bfs

    if curr_idx == n*n:
        return

    if curr_cnt == k:
        bfs()
        ans_cnt = max(ans_cnt, cnt_in_bfs)
        return

    next_vertex = backtracking_grid[curr_idx]
    selected_group.append(next_vertex)
    selected_city(curr_cnt+1, curr_idx+1)
    selected_group.pop()
    selected_city(curr_cnt, curr_idx + 1)


selected_city(0, 0)
print(ans_cnt)