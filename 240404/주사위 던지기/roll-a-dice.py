n, m, r, c = tuple(map(int, input().split()))
Ro_arr = list(input().split())
grid = [[0]*n for _ in range(n)]
x,y = r -1 , c-1
# L, R, U, D 방향
dir_r, dir_c = [0,0,-1,1], [-1,1,0,0]

# 현재 밑에 있는 숫자, 왼쪽 숫자(L), 앞에 있는 숫자(D).
dice = [6, 4, 2]

# L이나 R로 회전하면, 앞과 뒤쪽에 있는 숫자는 그대로이고,
# U나 D로 회전하면, 왼쪽과 오른쪽에 있는 숫자가 그대로이다.
# 따라서, 주사위가 회전하면, 위 공식에 맞게 주사위 숫자를 바꿔주면된다.

def In_Range(x,y):
    return x >= 0 and x < n and y >= 0 and y < n

def Move(d) :
    global x,y
    dx, dy = x + dir_r[d], y + dir_c[d]
    if In_Range(dx, dy) :
        x,y = dx, dy
        Rotate(d)


def Rotate(d):
    bottom_num = dice[0] # 현재 바닥에 있는 숫자
    if d == 0 :
        dice[0] = dice[1]           # 왼쪽에 있던 숫자가 바닥으로, 오른쪽에 있던 숫자가 위로
        dice[1] = 7 - bottom_num    # 바닥에 있는 숫자가 오른쪽으로 갔으므로
        #dice[2] = dice[2]          # 앞에 있는 숫자는 그대로
    elif  d == 1 :
        dice[0] = 7 - dice[1]       # 오른쪽에 있던 숫자가 바닥으로, 왼쪽에 있던 숫자가 위로
        dice[1] = bottom_num        # 바닥에 있는 숫자가 왼쪽으로 간다.
    elif d == 3 :
        dice[0] = dice[2]           # 앞에 있던 숫자가 바닥으로, 뒤에 있던 숫자가 위로 온다.
        dice[2] = 7 - bottom_num    # 바닥에 있는 숫자가 뒤로 갔으므로
    else :
        dice[0] = 7 - dice[2]       # 뒤에 있던 숫자가 바닥으로, 앞에 있던 숫자가 위로 온다.
        dice[2] = bottom_num        # 바닥에 있는 숫자



dir_num = 0
ans = 0
grid[x][y] = dice[0]
for ro in Ro_arr:
    direction = 0
    if ro == 'R' :
        direction = 1
    elif ro == 'U' :
        direction = 2
    elif ro == 'D' :
        direction = 3
    else :
        direction = 0

    Move(direction)
    grid[x][y] = dice[0]

for row in grid :
    for elem in row :
        ans += elem
print(ans)