n,t = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(2)
]

def move() :
    # 둘째줄
    temp2 = grid[0][n-1]
    temp1 = grid[1][n-1]
    for j in range(n-1, 0, -1) :
        grid[1][j] = grid[1][j-1]
    grid[1][0] = temp2

    # 첫째줄
    for j in range(n-1, 0, -1) :
        grid[0][j] = grid[0][j-1]
    grid[0][0] = temp1


for _ in range(t):
    move()


for row in grid:
    for elem in row:
        print(elem, end = ' ')
    print()