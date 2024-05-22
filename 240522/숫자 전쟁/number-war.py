n = int(input())
player1 = [0] + list(map(int, input().split()))
player2 = [0] + list(map(int, input().split()))

# dp[i][j] : player2의 i번째 카드가 j 번째 
dp = [[-1]* (n+1) for _ in range(n+1)]

dp[0][0] = 0

for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            continue

        # 첫번째 플레이어가 더 작은 경우 : 첫 번째 플레이어의 카드를 버리고
        # 점수는 변경되지 않음
        if player2[j+1] > player1[i+1]:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        
        # 두번째 플레이어가 더 작은 경우 : 두 번째 플레이어의 카드를 버리고,
        # 두 번째 플레이어의 카드 값만큼 점수를 추가한다.
        if player2[j+1] < player1[i+1]:
            dp[i][j+1] = max(dp[i][j+1], dp[i][j] + player2[j+1])
            
        # 카드버리기
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])


ans = 0
for i in range(n+1):
    ans = max(ans, dp[i][n])
    ans = max(ans, dp[n][i])

print(ans)