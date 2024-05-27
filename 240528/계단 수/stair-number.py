MOD = 10**9+7

n = int(input())

#dp[i][j] : i 번째에 j를 선택했을때의 계단 수의 개수
dp = [[0]*10 for _ in range(n+1)]

for i in range(1, 10):
    dp[1][i] = 1


for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][0] = dp[i-1][1]
        elif j == 9:
            dp[i][9] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        

#123, 323, 343, 543
#2123, 4323,2323, 2343, 4343, 6543, 4543

print(sum(dp[n][::]) % MOD)