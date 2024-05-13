n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
ans = 0

dp = [[0]*n for _ in range(n)]

#초기값 세팅
dp[0][0] = grid[0][0]

for i in range(1, n):
    dp[0][i] = dp[0][i - 1] + grid[0][i]
    dp[i][0] += dp[i-1][0] + grid[i][0]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + grid[i][j]

print(max(dp[n-1][:]))