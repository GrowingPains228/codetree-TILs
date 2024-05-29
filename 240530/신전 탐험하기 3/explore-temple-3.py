n, m = tuple(map(int, input().split()))

floors = [[0, 0, 0]]
for _ in range(n):
    floors.append(list(map(int, input().split())))

#dp[i][j] : i번째 층에서, j번째 방을 선택 했을때,
dp = [[0]*(m) for _ in range(n+1)]
for i in range(m):
    dp[1][i] = floors[1][i]

for i in range(2, n+1):
    for j in range(m):
        for k in range(m):
            if j == k:
                continue

            dp[i][j] = max(dp[i][j], dp[i-1][k] + floors[i][j])

print(max(dp[n]))