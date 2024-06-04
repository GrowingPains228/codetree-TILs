n = int(input())
players = [(0,0)]
for _ in range(n):
    s, b = tuple(map(int, input().split()))
    players.append((s, b))

# i번째 학생까지 선택했을때, 축구 j 명, 야구 k 명 선택했을 때의 최대 능력합
dp = [[[0]*10 for _ in range(12)] for _ in range(n+1)]
# 초기화
soccer, baseball = players[1]
dp[1][1][0] = soccer
dp[1][0][1] = baseball

for i in range(2, n+1):
    s, b = players[i]
    for j in range(1, 12):
        for k in range(1, 10):
            dp[i][j][k] = max(dp[i-1][j-1][k] + s, dp[i-1][j][k-1] + b)


print(dp[n][11][9])