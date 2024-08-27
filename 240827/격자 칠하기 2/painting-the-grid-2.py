# Parametric Search + BFS
MAX_DIFF = 10**6
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]  #상, 하, 좌, 우 순서
visited = [[False] * n for _ in range(n)]

def InRange(r, c):
    return 0 <= r < n and 0 <= c < n


def Movable(r, c, nr, nc, diff):
    return not visited[nr][nc] and abs(matrix[r][c] - matrix[nr][nc]) <= diff


def CanBeAnswer(value):
    return n*n // 2 <= value


def BFS(r, c, diff):
    dq = list()
    dq.append((r, c))
    visited[r][c] = True
    cnt = 1
    while dq:
        c_r, c_c = dq.pop()
        for dr, dc in zip(drs, dcs):
            nr, nc = c_r + dr, c_c + dc
            if InRange(nr, nc) and Movable(c_r, c_c, nr, nc, diff):
                visited[nr][nc] = True
                dq.append((nr, nc))
                cnt += 1
    return cnt


def is_possible(diff):
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    cnt_colors = 0
    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                cnt_colors = max(cnt_colors, BFS(r,c, diff))

    return CanBeAnswer(cnt_colors)


left, right = 1, MAX_DIFF
ans = MAX_DIFF
while left <= right:
    mid = (left + right)//2
    if is_possible(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1
print(ans)