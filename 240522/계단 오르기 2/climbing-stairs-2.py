import sys
INT_MIN = sys.maxsize

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [[0]*4 for _ in range(n+1)]
dp[1][1] = arr[1]
dp[2][0] = arr[2]
dp[2][2] = arr[1] + arr[2]

# dp[i][j] : i번 계단에 도착했을때, 정확히 j번 1계단 올랐을 때의 최대 가치
for i in range(3, n+1):
    for j in range(4):
        # 2번 점프하는 경우
        if dp[i-2][j] != 0:
            dp[i][j] = max(dp[i][j], dp[i-2][j] + arr[i])

        # 1번 점프하는 경우
        if j and dp[i-1][j-1] != 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + arr[i])

print(max(dp[n]))