a = input()
b = input()

len_a, len_b = len(a), len(b)
a = " " + a
b = " " + b

dp = [[0]*(len_b+1) for _ in range(len_a+1)]

# 제일 첫 행열 초기화
for i in range(1, len_a+1):
    dp[i][0] = i

for i in range(1, len_b+1):
    dp[0][i] = i


for i in range(1, len_a + 1):
    for j in range(1, len_b + 1):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = min(dp[i-1][j-1] + 2, dp[i-1][j]+1, dp[i][j-1]+1)


print(dp[len_a][len_b])