n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [[0]*n for _ in range(n)]


def initialize():
    dp[0][0] = grid[0][0]
    for i in range(1,n):
        dp[0][i] = min(dp[0][i-1], grid[0][i])
        dp[i][0] = min(dp[i-1][0], grid[i][0])


initialize()
for i in range(1, n):
    for j in range(1,n):
        if dp[i][j-1] <= grid[i][j] and dp[i-1][j] <= grid[i][j]:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        elif dp[i][j-1] >= grid[i][j] and dp[i-1][j] >= grid[i][j]:
            dp[i][j] = grid[i][j]
        elif grid[i][j] > dp[i-1][j] :
            dp[i][j] = max(grid[i][j], dp[i][j-1])
        else:
            dp[i][j] = max(grid[i][j], dp[i-1][j])
print(dp[n-1][n-1])