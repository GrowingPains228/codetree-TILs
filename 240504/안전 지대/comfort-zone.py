n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
# K의 범위는 가능 큰 높이 만큼 으로 설정
MAX_RANGE = max([max(row) for row in grid])
MIN_RANGE = min([min(row) for row in grid])
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]


def In_range(x,y):
    return 0 <= x < n and 0 <= y < m


def can_go(x, y, k):
    if not In_range(x,y):
        return False

    if grid[x][y] <= k or visited[x][y] :
        return False

    return True


def dfs(x, y, k):
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]  # 아래, 위, 왼쪽, 오른쪽

    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, k):
            dfs(nx, ny, k)


def simulation():
    global visited

    ans_k, ans_cnt = 1, 0
    for height in range(MIN_RANGE, MAX_RANGE+1):
        # 초기화
        visited = [
            [False for _ in range(m)]
            for _ in range(n)
        ]
        cnt = 0

        # n*m 만큼 돌면서 영역 세기
        for i in range(n):
            for j in range(m):
                if grid[i][j] > height and not visited[i][j]:
                    cnt += 1
                    dfs(i, j, height)

        # 영역을 다 돌았으면 갯수 갱신
        if ans_cnt < cnt:
            ans_cnt = cnt
            ans_k = height
        
        if cnt == 0:
            break

    return ans_k, ans_cnt


height_K, count = simulation()
print(height_K, count)