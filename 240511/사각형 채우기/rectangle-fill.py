MAX_SIZE = 1000
MOD = 10007

n = int(input())
dp = [0] * (MAX_SIZE + 1)

dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, MAX_SIZE+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%MOD)