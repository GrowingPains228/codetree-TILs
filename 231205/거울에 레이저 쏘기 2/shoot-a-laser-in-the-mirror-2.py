n = int(input())

dxs, dys = [1,0,-1,0], [0,1,0,-1]

# 격자 세팅
mirror_Room = [
    list(input()) for _ in range(n)
]

direct_type = 0

def in_range(x,y) :
    return 0 <= x and x < n and 0 <= y and y < n

# /,\ 에 따른 방향 바뀌는 공식
def cal_dir(x,y) :
    global direct_type
    if mirror_Room[x][y] == '/' :
        if direct_type in (0,2) :
            direct_type = (direct_type + 3) % 4
        else :
            direct_type = (direct_type + 1) % 4
    else : # arr[x][y] == '\'
        if direct_type in (0,2) :
            direct_type = (direct_type + 1) % 4
        else :
            direct_type = (direct_type + 3) % 4

# 발사 지점 번호
start_num = int(input())
# 초기 시작 위치 및 방향 판별
r,c = -1,-1
if 1 <= start_num and start_num <= n :
    direct_type = 0
    r = -1
    c = start_num -1
elif n + 1 <= start_num and start_num <= 2*n :
    direct_type = 3
    c = n 
    r = start_num - n -1
elif 2*n + 1 <= start_num and start_num <= 3*n :
    direct_type = 2
    r = n
    c = n - (start_num - 2 * n)
else :
    direct_type = 1
    c = -1
    r = n - (start_num - 3 * n)

x,y = r, c

# 메인 시작 전 초기 세팅
cnt = 0
dx, dy = x + dxs[direct_type], y + dys[direct_type]

while in_range(dx,dy) :
    x,y = dx, dy
    cnt += 1
    cal_dir(x, y)
    dx, dy = x + dxs[direct_type], y + dys[direct_type]

print(cnt)