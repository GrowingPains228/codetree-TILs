import sys
sys.setrecursionlimit(10**4)

MAX_NUM = 10**9
# 입력
m, n = tuple(map(int, input().split()))
Matrix = [list(map(int, input().split())) for _ in range(m)]
Colored_Matrix = [list(map(int, input().split())) for _ in range(m)]

# 변수 선언
blocks = list()
for i in range(m):
    for j in range(n):
        if Colored_Matrix[i][j] == 1:
            blocks.append((i,j))
drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[False] * n for _ in range(m)]


def In_Range(nr, nc):
    return 0 <= nr < m and 0 <= nc < n


def Movable(r, c, nr, nc, diff):
    return not visited[nr][nc] and abs(Matrix[nr][nc] - Matrix[r][c]) <= diff


def BFS(r, c, diff):
    q = list()
    q.append((r,c))
    visited[r][c] = True

    while q:
        cur_r, cur_c = q.pop()
        for (dr, dc) in zip(drs, dcs):
            nr, nc = cur_r + dr, cur_c + dc
            if In_Range(nr, nc) and Movable(cur_r, cur_c, nr, nc, diff):
                visited[nr][nc] = True
                q.append((nr, nc))


def DFS(r, c, diff):
    if visited[r][c]:
        return

    visited[r][c] = True
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if In_Range(nr, nc) and Movable(r, c, nr, nc, diff):
            DFS(nr, nc, diff)


def IsPossible(diff):
    for i in range(m):
        for j in range(n):
            visited[i][j] = False

    # 색칠된 곳들 중 한곳에서 출발했을때, 모든 색칠한 블럭이 True면 모두 도달한 것임.
    r, c = blocks[0]
    #BFS(r, c, diff)
    DFS(r, c, diff)

    for (br, bc) in blocks:
        if not visited[br][bc]:
            return False

    return True


left, right = 0, MAX_NUM
ans = MAX_NUM
while left <= right:
    mid = (left + right) // 2
    if IsPossible(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)