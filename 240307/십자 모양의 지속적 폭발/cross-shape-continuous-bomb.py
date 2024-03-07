NONE = -1
n,m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0]*n
    for _ in range(n)
]


def choose(colum):
    for i in range(n):
        if not grid[i][colum]:
            continue
        
        Bomb(i, colum)
        break

def in_bomb_range(x, y, center_x, center_y, bomb_range):
    return (x == center_x or y == center_y) and abs(x - center_x) + abs(y - center_y) < bomb_range


# 범위안에 있으면 폭발
def Bomb(r,c):
    bomb_range = grid[r][c]
    for i in range(n):
            for j in range(n):
                if in_bomb_range(i, j, r, c, bomb_range):
                    grid[i][j] = 0
    

# 중력 받아 떨어지게 하기
def Drop():
    # 초기화
    for i in range(n):
         for j in range(n):
            next_grid[i][j] = 0
    
    for i in range(n):
        next_idx = n-1
        for j in range(n-1, -1, -1):
            if not grid[j][i]:
                continue
            
            next_grid[next_idx][i] = grid[j][i]
            next_idx -= 1
    
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]


# 입력 받기
for _ in range(m):
    choose(int(input())-1)
    Drop()


# 출력
for row in grid:
    for elem in row:
        print(elem, end = " ")
    print()