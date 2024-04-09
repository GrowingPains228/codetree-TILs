n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
ans = 0
# 진행방향이 U(0), D(1), R(2), L(3) 이 있는데,
# '/'(1) 블록인 경우 : D -> L, L -> D, R -> U, U -> R ; + 2
# '\'(2) 블록인 경우 : D -> R, R -> D, L -> U, U -> L ; + 3
dxs, dys = [ -1, 1, 0, 0 ], [ 0, 0, 1, -1 ]

def ChangeDir_byChar(x, y, d) :
    if grid[x][y] == 1 :          #'/'
        return (d + 2)%4
    elif grid[x][y] == 2 :        #'\'
        if d in (1, 3):
            return (d + 1)%4
        else:
            return (d + 3)%4
    else :                  # 아무것도 없음
        return d


def InRange(x,y):
    return x >= 0 and x < n and y >= 0 and y < n


# 시작 지점과 출발 방향을 인자로 받아서, 빠져나오는데 총 걸린시간을 계산하는 움직이는 시뮬레이션 함수
def Move(x, y, d):
    time = 0
    # 첫 출발은 범위 밖에서 출발하므로 무조건 한번 실행한다.
    # 실행해 보고, 범위 안이라면 계속 진행
    dx, dy = x + dxs[d], y + dys[d]
    if not InRange(dx, dy):
        return 0
    else : # 첫 출발을 진행한 후, 빠져 나올때까지 무한 실행
        x,y = dx, dy
        time += 1
        while True :
            d = ChangeDir_byChar(x, y, d)
            dx, dy = x + dxs[d], y + dys[d]
            if not InRange(dx, dy): # 빠져 나오기
                time += 1
                break
            x,y = dx, dy
            time += 1
    return time


def simulation():
    global ans
    # 윗 부분에서 시작할때 x = -1, 방향 : D(1)
    for i in range(n):  
        ans = max(ans, Move(-1, i, 1))
    
    # 아랫 부분에서 시작 x = n, 방향 : U(0)
    for i in range(n):  
        ans = max(ans, Move(n, i, 0))

    # 왼쪽 부분에서 시작 y = -1, 방향 : R(2)
    for i in range(n):  
        ans = max(ans, Move(i, -1, 2))

    # 오른쪽 부분에서 시작 y = n, 방향 : L(3)
    for i in range(n):  
        ans = max(ans, Move(i, n, 3))


simulation()
print(ans)