n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
        [0]*n for _ in range(n)
]
dp_max = [
        [0]*n for _ in range(n)
]
dp_min = [
        [0]*n for _ in range(n)
]


def initialize():
    dp_max[0][0] = grid[0][0]
    dp_min[0][0] = grid[0][0]

    for i in range(1, n):
        dp_max[0][i] = max(dp_max[0][i-1], grid[0][i])
        dp_min[0][i] = min(dp_min[0][i-1], grid[0][i])

        dp_max[i][0] = max(dp_max[i - 1][0], grid[i][0])
        dp_min[i][0] = min(dp_min[i - 1][0], grid[i][0])


initialize()
for i in range(1, n):
    for j in range(1, n):
        if (max(grid[i][j],dp_max[i][j-1]) - min(grid[i][j],dp_min[i][j-1])
                > max(grid[i][j],dp_max[i-1][j]) - min(grid[i][j],dp_min[i-1][j])):
            dp_max[i][j] = max(grid[i][j], dp_max[i-1][j])
            dp_min[i][j] = min(grid[i][j], dp_min[i-1][j])
        elif (max(grid[i][j],dp_max[i][j-1]) - min(grid[i][j],dp_min[i][j-1])
                < max(grid[i][j],dp_max[i-1][j]) - min(grid[i][j],dp_min[i-1][j])):
            dp_max[i][j] = max(grid[i][j], dp_max[i][j-1])
            dp_min[i][j] = min(grid[i][j], dp_min[i][j-1])
        else:
            if dp_max[i][j-1] > dp_max[i-1][j]:
                dp_max[i][j] = max(grid[i][j], dp_max[i-1][j])
                dp_min[i][j] = min(grid[i][j], dp_min[i - 1][j])
            elif dp_max[i][j-1] < dp_max[i-1][j]:
                dp_max[i][j] = max(grid[i][j], dp_max[i][j - 1])
                dp_min[i][j] = min(grid[i][j], dp_min[i][j - 1])
            else:
                if dp_min[i][j-1] >= dp_min[i-1][j]:
                    dp_max[i][j] = max(grid[i][j], dp_max[i - 1][j])
                    dp_min[i][j] = min(grid[i][j], dp_min[i - 1][j])
                else:
                    dp_max[i][j] = max(grid[i][j], dp_max[i][j - 1])
                    dp_min[i][j] = min(grid[i][j], dp_min[i][j - 1])
                    
print(dp_max[n-1][n-1] - dp_min[n-1][n-1])