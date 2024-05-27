n = int(input().rstrip())

rooms = [[0, 0, 0]]
for _ in range(n):
    left, middle, right = map(int, input().rstrip().split())
    rooms.append((left, middle, right))

# dp[i][j] : i 번째 층에서 j를 방을 선택 했을때 최대 보물 개수 ( j=0 : left, j=1 : middle, j=2 : right )
dp = [[0]*3 for _ in range(n+1)]
dp[1][0], dp[1][1], dp[1][2] = rooms[1][0], rooms[1][1], rooms[1][2]

for i in range(2, n+1):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue

            dp[i][j] = max(dp[i][j], dp[i-1][k] + rooms[i][j])
            
print(max(dp[n][::]))