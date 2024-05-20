import sys
INT_MIN = -sys.maxsize
n,m = tuple(map(int, input().split()))
weight = [0] * (n + 1)
value = [0] * (n + 1)
for i in range(1, n+1):
    weight[i], value[i] = tuple(map(int, input().split()))


dp = [
    [INT_MIN] * (m+1)
    for _ in range(n+1)
]

dp[0][0] = 0

for i in range(1, n+1):
    for j in range(m+1):
        if j >= weight[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight[i]] + value[i])
        else:
            dp[i][j] = dp[i-1][j]

ans = 0
for j in range(m+1):
    ans = max(ans, dp[n][j])

print(ans)