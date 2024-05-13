import sys
MAX_SIZE = sys.maxsize
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [[MAX_SIZE]*n for _ in range(n)]


def Initialize():
    dp[0][n-1] = grid[0][n-1]

    # 제일 위쪽 초기화
    for i in range(n-2, -1, -1):
        dp[0][i] = dp[0][i+1] + grid[0][i]

    # 제일 오른쪽 열 초기화
    for i in range(1, n):
        dp[i][n - 1] = dp[i - 1][n - 1] + grid[i][n - 1]


Initialize()
for i in range(1, n):
    for j in range(n-2, -1, -1):
        dp[i][j] = grid[i][j] + min(dp[i-1][j],  dp[i][j+1])

print(dp[n-1][0])