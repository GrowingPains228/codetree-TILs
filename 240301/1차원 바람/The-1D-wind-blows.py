N,M,Q = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

#오른쪽 왼쪽으로 이동할때
def Move(index, direction) :
    temp = 0
    if direction == 'R' : # 오른쪽
        temp = grid[index][0]
        for j in range(M-1) :
            grid[index][j] = grid[index][j+1]
        grid[index][M-1] = temp
    else : # 왼쪽
        temp = grid[index][M-1]
        for j in range(M-1, 0, -1) :
            grid[index][j] = grid[index][j-1]
        grid[index][0] = temp

def Move_Up(index, direction):
    while index - 1 >= 0 and check_avable(index, index-1) :
        index -= 1
        if direction == 'R' :
            Move(index, 'L')
            direction = 'L'
        else :
            Move(index, 'R')
            direction = 'R'

def Move_Down(index, direction):
    while index + 1 < N and check_avable(index, index+1) :
        index += 1
        if direction == 'R' :
            Move(index, 'L')
            direction = 'L'
        else :
            Move(index, 'R')
            direction = 'R'

def check_avable(index1, index2) :
    return any([
        grid[index1][col] == grid[index2][col]
        for col in range(M)
    ])

for _ in range(Q) :
    r, d = input().split()
    Move(int(r)-1, d)
    Move_Up(int(r)-1, d)
    Move_Down(int(r)-1, d)

for row in grid:
    for elem in row:
        print(elem, end = " ")
    print()