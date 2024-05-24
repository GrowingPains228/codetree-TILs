MAX_RANGE = 20
MIN_RANGE = -20
n, m = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

#  0 이상 40 이하로 있다고 조정한다.

# dp[i][j]를 정의한다.
# i번째 수를 (+)하거나 (-)했을때, 나온 결과값이 j일때, 최대 횟수의 값
dp = [[0]*(MAX_RANGE*2+1) for _ in range(n+1)]
dp[0][MAX_RANGE] += 1

# n번째 전 까지 구한다.
for i in range(n):
    for j in range(MAX_RANGE*2+1):
        if dp[i][j] == 0:
            continue

        if nums[i] == 0:
            dp[i+1][j] = dp[i][j] * 2
        else:
            if j - nums[i] >= 0:
                dp[i+1][j-nums[i]] = dp[i+1][j-nums[i]] + dp[i][j]

            if j + nums[i] <= MAX_RANGE*2:
                dp[i+1][j+nums[i]] = dp[i+1][j+nums[i]] + dp[i][j]

print(dp[n][MAX_RANGE + m])