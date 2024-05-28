n = int(input().rstrip())

rooms = [[0, 0, 0]]

for _ in range(n):
    left, middle, right = tuple(map(int, input().rstrip().split()))
    rooms.append([left, middle, right])

# dp[i][j][k] : i방향룸을 시작으로 j층에서 k방향 방으로 끝난 보물의 최대값
dp = [[[0]*3 for _ in range(n+1)]for _ in range(3)]

#left = 0, middle = 1, right = 2
for i in range(3):
    for j in range(3):
        dp[i][1][j] = rooms[1][i]

for i in range(3):
    for j in range(3):
            if j == i:
                dp[i][2][j] = 0
            else:
                dp[i][2][j] = dp[i][1][j] + rooms[2][j]


for i in range(3):
    for j in range(3, n+1):
        for k in range(3):
            for z in range(3):
                if k == z :
                    continue

                dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][z] + rooms[j][k])

ans = 0
        
for i in range(3):
    for j in range(3):
        if i == j:
            continue

        ans = max(ans, dp[i][n][j])

print(ans)