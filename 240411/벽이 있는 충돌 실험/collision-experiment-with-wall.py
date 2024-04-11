T = int(input())
mapper = {
    'U' : 0,
    'R' : 1,
    'D' : 2,
    'L' : 3
}
count = []
next_count = []
direct = []
next_direct = []
n = 0

def In_Range(x,y) :
    return x >= 0 and y >= 0 and x < n and y < n


def Get_MovePos(x,y):
    d = direct[x][y]
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    nx, ny = x + dxs[d], y + dys[d]
    #다음 위치가 범위 밖으로 나간다면, 벽에 튕기는 것이다.
    if not In_Range(nx,ny) :
        d = (d + 2) % 4
        nx, ny = x, y

    # 그게 아니라면, 다음 위치로 이동할 것임.
    return nx, ny, d


def Move(x,y):
    nx, ny, nd = Get_MovePos(x, y)
    next_count[nx][ny] += 1
    next_direct[nx][ny] = nd


def all_Move():
    global n, next_count, next_direct
    next_count = [[0]*n for _ in range(n)]
    next_direct = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if count[i][j] :
                Move(i, j)
                
    # Copy + 충돌 체크하면서
    for i in range(n) :
        for j in range(n) : 
            if next_count[i][j] >= 2:
                next_count[i][j] = 0
                next_direct[i][j] = -1

            count[i][j] = next_count[i][j]
            direct[i][j] = next_direct[i][j]


for _ in range(T):
    N,M = tuple(map(int, input().split()))
    n = N
    count = [[0]*n for _ in range(n)]
    direct = [[-1]*n for _ in range(n)]
 
    for _ in range(M):
        x,y,d = tuple(input().split())
        x,y = int(x)-1, int(y)-1
        d = mapper[d]
        count[x][y] += 1
        direct[x][y] = d
    
    for _ in range(2*N):
        all_Move()
        
    ans = sum([
        count[i][j] for i in range(n)
        for j in range(n)
    ])
    print(ans)