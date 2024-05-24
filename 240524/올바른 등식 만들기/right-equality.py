MAX_RANGE = 20
MIN_RANGE = -20
n, m = tuple(map(int, input().split()))
nums = [20] + list(map(int, input().split()))

#  0 이상 40 이하로 있다고 조정한다.

# dp[i][j]를 정의한다.
# i번째 수를 (+)하거나 (-)했을때, 나온 결과값이 j일때, 최대 횟수의 값
dp = [[0]*(MAX_RANGE*2+1) for _ in range(n+1)]
dp[0][nums[0]] = 1
for i in range(1, n+1):
    for j in range(MAX_RANGE*2+1):
        if j - nums[i] >= 0 and dp[i-1][j-nums[i]] != 0:
            dp[i][j] = dp[i-1][j-nums[i]]

        if j + nums[i] <= MAX_RANGE*2 and dp[i-1][j+nums[i]] != 0:
            if dp[i][j]:
                dp[i][j] = max(dp[i-1][j+nums[i]], dp[i][j]) + 1
            else:
                dp[i][j] = dp[i-1][j+nums[i]]

print(dp[n][MAX_RANGE + m])