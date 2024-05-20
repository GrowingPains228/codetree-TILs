import sys
INT_MIN = -sys.maxsize
n = int(input())
value = [0] + list(map(int, input().split()))
dp = [INT_MIN] * (n+1)
dp[0] = 0

for i in range(1, n+1):
    dp[i] = value[i]
    for j in range(i):
        dp[i] = max(dp[i], dp[i-j] + value[j])

print(max(dp))