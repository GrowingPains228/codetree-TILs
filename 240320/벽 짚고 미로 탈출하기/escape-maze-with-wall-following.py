UNESCAPE = -1
n = int(input())
x,y = tuple(map(int, input().split()))

grid = [
    list(input())
    for _ in range(n)
]
second = 0
cur_dir = 0
# 오른쪽=0 / 아래쪽=1 / 왼쪽=2 / 위쪽=3
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

x ,y = x - 1, y - 1

def in_range(x,y):
    return x >= 0 and y >= 0 and x < n and y < n


def Move():
    global second, cur_dir, x, y
    nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
    x,y = nx, ny
    second += 1


def Auto_Rotate():
    global cur_dir
    count_check = 4
    # 바라 보고 있는 방향에 벽이 존재하는 경우, 벽이 없을때까지 돌아주기
    # 근데, 총 4번 돌았다면, 그건 사방이 벽으로 막혀있는 경우임.
    # 그러므로 -1출력
    for _ in range(4):
        nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
        if in_range(nx, ny) and grid[nx][ny] == '#':
            cur_dir = (cur_dir + 3) % 4
            count_check -= 1
        else :
            break;
        
    # 돌다 왔는데, 제자리라면 그건 사방이 벽으로 막힌경우
    if not count_check:
        return False
    else:
        return True


def check_Wall():
    global cur_dir
    # 이동한 위치 오른쪽에 벽이 없는 경우
    rx, ry = x + dxs[(cur_dir + 1) % 4], y + dys[(cur_dir + 1)%4]
    if in_range(rx, ry) and grid[rx][ry] == '.' :
        cur_dir = (cur_dir + 1) % 4
        Move()

while in_range(x,y) :
     tf = Auto_Rotate()
     Move()
     check_Wall()

     if second > n*n or not tf:
        second = UNESCAPE
        break

print(second)