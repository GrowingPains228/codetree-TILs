import sys
MOD = 10**9 + 7
# n일을 살아남기 위해서 만들 수 있는 n자리의 평가 문자열의 가짓수
n = int(input())

# dp[i][j][k] : i 번째에 T를 j개 뽑았을 때, 연속으로 B를 k개 뽑는 가짓수
dp = [[[0]*3 for _ in range(3)] for _ in range(n+1)]

dp[1][0][0] = 1
dp[1][0][1] = 1
dp[1][1][0] = 1

for i in range(2, n+1):
    for j in range(3):
        for k in range(3):
            if k == 0:
                for z in range(max(0, j-1), j+1):
                    for t in range(3):
                        dp[i][j][k] += dp[i-1][z][t]
                        
            else:
                dp[i][j][k] = dp[i-1][j][k-1]

total = 0
for i in range(3):
    for j in range(3):
        total += dp[n][i][j]

print(total%MOD)