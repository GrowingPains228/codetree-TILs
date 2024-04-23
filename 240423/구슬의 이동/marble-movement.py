n, m, t, k = tuple(map(int, input().split()))
grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]

next_grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]


def In_Range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n


def Get_NextPos(x, y, v_num, move_dir):
    dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
    for _ in range(v_num):
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
        if not In_Range(nx, ny):
            move_dir = 3 - move_dir
            nx, ny = x + dxs[move_dir], y + dys[move_dir]
        
        x, y = nx, ny
    return (x, y, move_dir)


def Move_all():
    for x in range(n):
        for y in range(n):
            for (v, num, move_dir) in grid[x][y]:
                next_x, next_y, next_dir = Get_NextPos(x, y, v, move_dir)
                next_grid[next_x][next_y].append((v, num, next_dir))
    

def Select_marbles():
    for i in range(n):
        for j in range(n):
            if len(next_grid[i][j]) > k:
                next_grid[i][j].sort(key = lambda x : (-x[0], -x[1]))
                
                while len(next_grid[i][j]) > k:
                    next_grid[i][j].pop()


def simulate():
    # next_grid 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = []

    # 모든 구슬들 움직여 주기
    Move_all()

    # 각 칸마다 구슬이 최대 k 개만 남도록 조정
    Select_marbles()

    # 복사
    for x in range(n):
        for y in range(n):
            grid[x][y] = next_grid[x][y]


dir_mapper = {
    'U' : 0,
    'R' : 1,
    'L' : 2,
    'D' : 3
}

for i in range(m):
    r,c,d,v = tuple(input().split())
    r,c,v = tuple(map(int, [r,c,v]))

    grid[r-1][c-1].append((v, i+1, dir_mapper[d]))

for _ in range(t):
    simulate()

ans = sum([
    len(grid[i][j]) 
    for i in range(n)
    for j in range(n)
])

print(ans)