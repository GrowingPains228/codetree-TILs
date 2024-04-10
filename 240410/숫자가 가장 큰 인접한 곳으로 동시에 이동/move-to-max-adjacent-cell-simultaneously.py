# 입력 받기
n, m, t = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

count = [[0]*n for _ in range(n)]

for _ in range(m) :
    r,c = tuple(map(int, input().split()))
    count[r-1][c-1] = 1


def In_Range(r,c) :
    return r >= 0 and r < n and c >= 0 and c < n


def get_move_point(x,y) :
    oriValue = grid[x][y]
    # 상하좌우
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    id_x, id_y = x, y
    for dx, dy in zip(dxs, dys) :
        nx, ny = x + dx, y + dy
        if not In_Range(nx, ny) or grid[nx][ny] <= oriValue :
            continue
        
        # 더 큰 값을 가진 높으로 우선순위로 초기화
        (id_x, id_y) = (id_x, id_y) if grid[id_x][id_y] > grid[nx][ny] else (nx, ny)

    return (id_x, id_y)


def Simulation(time) :
    # 시간만큼
    for _ in range(time) :
        # 2차원 배열을 돌면서 객체를 이동시켜 준다.
        # next_Count = 초기화
        next_Count = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n) :
                if count[i][j] == 1:
                    x,y = get_move_point(i, j)
                    next_Count[x][y] += 1
        
        # 구슬 팅구면서 복사해주기
        for i in range(n) :
            for j in range(n) :
                if next_Count[i][j] >= 2 :
                    next_Count[i][j] = 0

                count[i][j] = next_Count[i][j]
        

Simulation(t)
ans = sum([
    count[i][j] for i in range(n)
    for j in range(n)
])

print(ans)