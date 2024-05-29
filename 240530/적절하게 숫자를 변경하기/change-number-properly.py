n,m = tuple(map(int, input().split()))
numbers = [0] + list(map(int, input().split()))

#dp[i][j][k] : i번째 수열까지 j번 다른 횟수이고 현재 k숫자 일때, 최대 유사도
dp = [[[0]* (5) for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, 5):
    dp[1][0][i] = 1 if numbers[1] == i else 0    

for i in range(2, n+1):
    for j in range(m+1):
        for k in range(1,5):
            for l in range(1, 5):
                if l == k:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + (numbers[i] == k))
                
                if l != k and j > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][l] + (numbers[i] == k))

ans = 0

for i in range(m+1):
    ans = max(ans, max(dp[n][i]))


print(ans)