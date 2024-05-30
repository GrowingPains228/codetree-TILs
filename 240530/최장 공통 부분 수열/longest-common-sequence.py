A = list(input())
B = list(input())

dp = [[0]*(len(A)) for _ in range(len(B))]


def initialize():
    dp[0][0] = 1 if A[0] == B[0] else 0

    for i in range(1, len(A)):
        dp[0][i] = 1 if A[i] == B[0] else dp[0][i-1]

    for i in range(1, len(B)):
        dp[i][0] = 1 if A[0] == B[i] else dp[i-1][0]


initialize()
for i in range(1, len(B)):
    for j in range(1, len(A)):
        if B[i] == A[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(max(dp[len(B)-1]))