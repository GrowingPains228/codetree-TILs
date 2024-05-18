MOD = 10007
n = int(input())
MAX_K = 3

num_arr = [1, 2, 5]
dp = [0] * (n+1)

dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    for j in range(MAX_K):
        if i >= num_arr[j]:
            dp[i] += dp[i-num_arr[j]]


print(dp[n] % MOD)


# '5'가 되는 경우
# 1이 되는 경우
# 2가 되는 경우
# 3이 되는 경우...
# 총 5가 되는 경우는 
#1. dp[4]경우에서 1을 더한 조합
#2. dp[3]의 경우에서 2를 더한것 조합

# '6'이 되는 경우
# dp[5] + 1
# dp[4] + 2
# dp[1] + 5