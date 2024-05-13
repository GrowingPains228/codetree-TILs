n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
        [[] for _ in range(n)]
        for _ in range(n)
]


def initialize():
    dp[0][0].append(grid[0][0]) # 최대 요소를 넣고
    dp[0][0].append(grid[0][0]) # 최소 요소를 넣는다
    for i in range(1,n):
        dp[i][0].append(max(dp[i-1][0][0], grid[i][0]))
        dp[i][0].append(min(dp[i-1][0][1], grid[i][0]))

        dp[0][i].append(max(dp[0][i-1][0], grid[0][i]))
        dp[0][i].append(min(dp[0][i-1][1], grid[0][i]))


initialize()
for i in range(1, n):
    for j in range(1, n):
        dp[i][j].append(max(grid[i][j], min(dp[i - 1][j][0], dp[i][j - 1][0])))
        dp[i][j].append(min(grid[i][j], max(dp[i - 1][j][1], dp[i][j - 1][1])))

print(dp[n-1][n-1][0] - dp[n-1][n-1][1])