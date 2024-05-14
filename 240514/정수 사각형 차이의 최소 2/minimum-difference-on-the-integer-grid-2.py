import sys

MAX_K = 100
INT_MAX = sys.maxsize

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [[0]*n for _ in range(n)]
ans = INT_MAX

#초기화 함수
def initialize():
    for i in range(n):
        for j in range(n):
            dp[i][j] = INT_MAX

    dp[0][0] = grid[0][0]

    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1],grid[0][i])
        dp[i][0] = max(dp[i-1][0],grid[i][0])


def sol(lower_bound):
    for i in range(n):
        for j in range(n):
            if grid[i][j] < lower_bound:
                grid[i][j] = INT_MAX
    

    for i in range(1,n):
        for j in range(1,n):
            dp[i][j] = max(grid[i][j], min(dp[i-1][j], dp[i][j-1]))

    return dp[n-1][n-1]


for lower_bound in range(1,MAX_K+1):
    initialize()
    upper_bound = sol(lower_bound)

    if upper_bound == INT_MAX:
        continue

    ans = min(ans, upper_bound - lower_bound)

print(ans)