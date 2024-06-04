n = int(input())
players = [(0,0)]
for _ in range(n):
    s, b = tuple(map(int, input().split()))
    players.append((s, b))

# i번째 학생까지 선택했을때, 축구 j 명, 야구 k 명 선택했을 때의 최대 능력합
dp = [[[0]*(n+1) for _ in range(10)] for _ in range(12)]
# 초기화
soccer, baseball = players[1]
dp[0][1][1] = baseball
dp[1][0][1] = soccer

for i in range(1, 12):
    for j in range(1, 10):
        for k in range(2, n+1):
            s, b = players[k]

            dp[i][j][k] = max(dp[i-1][j][k-1] + s, dp[i][j-1][k-1] + b)

print(max(dp[11][9]))