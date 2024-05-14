n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [[[] for _ in range(n)]
      for _ in range(n)]


def initialize():
    dp[0][0].append(grid[0][0])

    for i in range(1,n):
        dp[0][i] += dp[0][i-1]
        dp[0][i].append(grid[0][i])
        dp[0][i].sort()

        dp[i][0] += dp[i-1][0]
        dp[i][0].append(grid[i][0])
        dp[i][0].sort()

initialize()
for i in range(1,n):
    for j in range(1,n):
        max1, max2 = max(dp[i][j-1][-1], grid[i][j]), max(dp[i-1][j][-1], grid[i][j])
        min1, min2 = min(dp[i][j-1][0], grid[i][j]), min(dp[i-1][j][0], grid[i][j])
        dp1 = max1 - min1
        dp2 = max2 - min2
        if (-max1, min1) >= (-max2, min2):
            dp[i][j] += dp[i][j-1]
            dp[i][j].append(grid[i][j])
        else:
            dp[i][j] += dp[i-1][j]
            dp[i][j].append(grid[i][j])

        dp[i][j].sort()

print(max(dp[n-1][n-1]) - min(dp[n-1][n-1]))