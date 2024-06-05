import sys
n = int(input())
players = [(0,0)]
players.sort()
for _ in range(n):
    s, b = tuple(map(int, input().split()))
    players.append((s, b))

# i번째 학생까지 선택했을때, 축구 j 명, 야구 k 명 선택했을 때의 최대 능력합
dp = [[[-1]*(10) for _ in range(12)] for _ in range(n+1)]
# 초기화
dp[0][0][0] = 0
for i in range(1, n+1):
    soccer, baseball = players[i]
    for j in range(min(i+1, 12)):
        for k in range(min(i+1, 10)):
            if dp[i-1][j][k] != -1:
                dp[i][j][k] = dp[i-1][j][k]

            if k > 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1] + baseball)

            if j > 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k] + soccer)

print(dp[n][11][9])