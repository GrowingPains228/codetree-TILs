MAX_SIZE = 1000
MOD = 1000000007

n = int(input())
dp = [0] * (MAX_SIZE + 1)

dp[0] = 1
dp[1] = 2
dp[2] = 7 # dp[i-1] + dp[i-2] + (dp[i-1] + 2*dp[i-2]) = 2 * dp[i-1] + 3 * dp[i-2]
dp[3] = 2*dp[3-1] + 3*dp[3-2] + 2*dp[3-3]
dp[4] = 2*dp[4-1] + 3*dp[4-2] + 2*dp[4-3] + 2 * dp[4-4]

for i in range(3, MAX_SIZE+1):
    dp[i] = 2 * dp[i-1] + 3 * dp[i-2]
    for j in range(3, i+1):
        dp[i] += 2*dp[i-j]

print(dp[n] % MOD)