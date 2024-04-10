n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def In_Range(x,y) :
    return x >= 0 and x < n and y >= 0 and y < n


def Get_MovePosition(x,y):
    # 왼쪽 위에서 부터 시작
    dxs, dys = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
    max_idx, max_num = 0,0
    for (idx, (dx, dy)) in enumerate(zip(dxs, dys)):
        nx, ny = x + dx, y + dy
        if not In_Range(nx, ny):
            continue
        
        if max_num < grid[nx][ny] :
            max_idx = idx
            max_num = grid[nx][ny]
    
    return (x + dxs[max_idx], y + dys[max_idx])


def Move(x,y):
    (nx,ny) = Get_MovePosition(x,y)
    grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]


def Move_all():
    for x in range(1, n*n+1):
        for i in range(n):
            IsFind = False
            for j in range(n):
                if grid[i][j] == x:
                    IsFind = True
                    Move(i,j)
                    break
            if IsFind:
                break    
            

def Simulation(t):
    for _ in range(t):
        Move_all()


Simulation(m)

for row in grid :
    for elem in row:
        print(elem, end = " ")
    print()