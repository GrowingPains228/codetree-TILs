MAX_SIZE = 19
n = int(input())

dp = [0]* (MAX_SIZE + 1)
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 5 # 2*dp[3-1] + 1

# BST를 만드는 방법을 알아야 하는데,
# 그림으로 그려보니
#dp[4] = 2*dp[4-1]*dp[0] + 2*dp[4-2]*dp[1]
#dp[5] = 2*dp[5-1]*dp[0] + 2*dp[5-2]*dp[1] + dp[5-3]*dp[2]
#dp[6] = 2*dp[6-1]*dp[0] + 2*dp[6-2]*dp[1] + 2*dp[6-3]*dp[2]
#dp[7] = 2*dp[7-1]*dp[0] + 2*dp[7-2]*dp[1] + 2*dp[7-3]*dp[2] + dp[7-4]*dp[3]
# dp[8] = 2*dp[8-1]*dp[0] + 2*dp[8-2]*dp[1] + 2*dp[8-3]*dp[2] + 2*dp[8-4]*dp[3]
# ... 이런 규칙이 있는 것을 관찰할 수 있었음.
# dp[n] =
for i in range(4, MAX_SIZE + 1):
    max_idx = i//2
    for j in range(1, max_idx+1):
        dp[i] += 2*dp[i-j]*dp[j-1]

    if i % 2 != 0:
        dp[i] += dp[i - (max_idx+1)]*dp[max_idx]

print(dp[n])