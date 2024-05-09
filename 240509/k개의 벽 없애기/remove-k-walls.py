from collections import deque
# 입력
n, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
x1, y1 = tuple(map(int, input().split()))
x1, y1 = x1 - 1, y1 - 1
x2, y2 = tuple(map(int, input().split()))
x2, y2 = x2 - 1, y2 - 1

# 벽 뽑아내기
wall_pos_group = [
    (i,j) for i in range(n)
    for j in range(n)
    if grid[i][j]
]
selected_wall_group = []

# bfs 변수
visited = [[False]*n for _ in range(n)]
step = [[0]*n for _ in range(n)]
queue = deque()

# 정답 출력 변수
ans = n*n

# backtracking 으로 조합을 통해 벽을 k개 뽑아서 없애주고,
# bfs를 통해 최단  거리 탐색
# 탐색 후에는, 도착지점에 도착했는지 판별해서
# 도착했다면, ans 에 최소 시간을 넣어주고
# 도착하지 못했다면, 일단 넘어간다.
# 전체를 다 돌고 나서, 그래도 도착하지 못했다면, ans = -1로 출력
def in_range(x,y):
    return 0 <= x < n and 0 <= y < n


def can_go(x,y):
    return in_range(x,y) and grid[x][y] == 0 and not visited[x][y]


def push(x,y,s):
    visited[x][y] = True
    queue.append((x,y))
    step[x][y] = s


def find_path():
    dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                push(nx, ny, step[x][y]+1)


def cal():
    # 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][j] = 0

    # 벽 제거 해주고
    for x, y in selected_wall_group:
        grid[x][y] = 0

    # 초기 위치 넣어주고
    push(x1, y1, 0)

    find_path()

    # 다시 되돌려 놓기
    for x, y in selected_wall_group:
        grid[x][y] = 1

    return step[x2][y2] if step[x2][y2] > 0 else n*n


def choose_wall(curr_cnt, curr_idx):
    global ans
    if curr_idx == len(wall_pos_group):
        if curr_cnt == k:
            ans = min(ans, cal())
        return

    selected_wall_group.append(wall_pos_group[curr_idx])
    choose_wall(curr_cnt + 1, curr_idx + 1)
    selected_wall_group.pop()
    choose_wall(curr_cnt, curr_idx + 1)


choose_wall(0,0)
print(ans if ans < n*n else -1)