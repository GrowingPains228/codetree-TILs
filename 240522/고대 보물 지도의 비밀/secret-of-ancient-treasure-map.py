import sys
UNUSED = -10001

n, k = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))

dp = [[UNUSED]*(k+1) for _ in range(n+1)]


ans = -sys.maxsize
# i번째를 선택했을 때 j번의 음수를 선택한 경우, 최댓값
for i in range(1, n+1):
    if arr[i] >= 0:
        for j in range(k+1):
            dp[i][j] = max(arr[i], dp[i-1][j] + arr[i])
            ans = max(ans, dp[i][j])
    else:
        for j in range(1, k+1):
            dp[i][j] = max(dp[i-1][j-1] + arr[i], arr[i])
            ans = max(ans, dp[i][j])

print(ans)