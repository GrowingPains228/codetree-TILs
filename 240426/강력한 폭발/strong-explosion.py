EMPTY = 0

n = int(input())
max_ans = 0
bomb_list = []
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
Next_grid = [
    [ EMPTY for _ in range(n)]
    for _ in range(n)
]

dxs = [
    [-2, -1, 0, 1, 2],
    [-1, 1, 0, 0, 0],
    [-1, -1, 0, 1, 1]
]
dys = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, -1],
    [-1, 1, 0, -1, 1]
]

def In_Range(x,y):
    return 0 <= x < n and 0 <= y < n


def Count_bomb_Area():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if Next_grid[i][j] :
                cnt += 1
    
    return cnt


def Resur_Bomb(bomb_idx):
    global max_ans
    if bomb_idx == len(bomb_list) :
        max_ans = max(max_ans, Count_bomb_Area())
        return
    
    for i in range(3):
        Bomb(bomb_idx, i)
        Resur_Bomb(bomb_idx + 1)
        Reset_bomb(bomb_idx, i)


def Bomb(idx, i):
    (x,y) = bomb_list[idx]
    for dx, dy in zip(dxs[i], dys[i]):
        nx, ny = x + dx, y + dy
        if In_Range(nx, ny):
            Next_grid[nx][ny] += 1


def Reset_bomb(idx, i):
    (x,y) = bomb_list[idx]
    for dx, dy in zip(dxs[i], dys[i]):
        nx, ny = x + dx, y + dy
        if In_Range(nx, ny):
            Next_grid[nx][ny] -= 1


# 총 폭탄의 위치를 세팅한다.
for i in range(n):
    for j in range(n):
        if grid[i][j] :
            bomb_list.append((i,j))


# 재귀 함수를 이용한 폭탄 연쇄 폭발.
Resur_Bomb(0)
print(max_ans)