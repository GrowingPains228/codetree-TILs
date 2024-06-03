A = input()
B = input()

len_A, len_B = len(A), len(B)
A = " " + A
B = " " + B
dp = [[0]*(len_B+1) for _ in range(len_A+1)]
for i in range(len_A+1):
    dp[i][0] = i

for i in range(len_B+1):
    dp[0][i] = i

for i in range(1, len_A+1):
    for j in range(1, len_B+1):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

print(dp[len_A][len_B])