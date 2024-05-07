from collections import deque
n, k = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [[False] * n for _ in range(n)]
queue = deque()
start_x, start_y = tuple(map(int, input().split()))
start_x -= 1
start_y -= 1
queue.append((start_x, start_y))
base_value = grid[start_x][start_y]


def in_range(x,y):
    return 0 <= x < n and 0 <= y < n


def can_go(x, y):
    if not in_range(x,y):
        return False

    if visited[x][y] or grid[x][y] >= base_value:
        return False

    return True


def Update_target_pos(x1, y1, x2, y2):
    if grid[x1][y1] == base_value:
        return x2, y2

    target1, target2 = grid[x1][y1], grid[x2][y2]

    if target1 > target2:
        return x1, y1
    elif target1 < target2:
        return x2, y2
    else:
        if x1 < x2:
            return x1, y1
        elif x1 > x2:
            return x2, y2
        else:
            return x1, y1 if y1 < y2 else y2


#그래프를 탐색하면서 이동할 수 있는 위치 업데이트
def bfs(tx, ty):
    t_x, t_y = tx, ty
    while queue:
        (x, y) = queue.popleft()
        dxs, dys = [-1, 1, 0, 0],[0, 0, 1, -1]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            # 탐색할 수 있는 위치면 계속 탐색
            # 탐색을 하면서 이동할 위치를 확인하고 계속 업데이트
            if can_go(nx, ny):
                visited[nx][ny] = True
                queue.append((nx, ny))
                t_x, t_y = Update_target_pos(t_x, t_y, nx, ny)
    return t_x, t_y


for i in range(k):
    visited = [[False] * n for _ in range(n)]
    visited[start_x][start_y] = True
    start_x, start_y = bfs(start_x, start_y)

    # 처음위치와 이동한 위치가 같다면, 이동하지 못하는 것임으로 종료
    # 그게 아니라면 계속 진행
    if base_value == grid[start_x][start_y]:
        break
    else :
        base_value = grid[start_x][start_y]
        queue.append((start_x, start_y))

print(start_x + 1, start_y + 1)