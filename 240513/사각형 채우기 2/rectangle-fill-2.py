n = int(input())
MAX_SIZE = 1000
dp = [0]* (MAX_SIZE+1)
dp[0] = 1
dp[1] = 1
dp[2] = 3

for i in range(3,n+1):
    dp[i] = dp[i-1]+ 2*dp[i-2]

print(dp[n])