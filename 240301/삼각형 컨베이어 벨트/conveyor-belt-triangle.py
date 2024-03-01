n,t = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(3)
]

def move(time):
    for _ in range(time) :
        end_value = grid[n-1][n-1]
        pre_temp = 0
        for i in range(n-1, -1, -1) :
            pe_temp = grid[i][n-1]
            for j in range(n-1, 0, -1) :
                grid[i][j] = grid[i][j-1]
            
            s = (i-1) if (i-1) >= 0 else 2
            grid[i][0] = grid[s][n-1]
        grid[0][0] = end_value

move(t)

for row in grid :
    for elem in row :
        print(elem, end = ' ')
    print()