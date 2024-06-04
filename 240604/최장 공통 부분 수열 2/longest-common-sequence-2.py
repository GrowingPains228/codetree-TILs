A = input()
B = input()

len_A, len_B = len(A), len(B)

# dp[i][j] : 문자열 A의 처음 i개 문자와 문자열 B의 처음 j개 문자가 이루는
# 최장 공통 부분 수열의 길이
dp = [[0]*(len_B+1) for _ in range(len_A+1)]
# 해당 경로를 저장하는 변수
path = [[(0,0)]*(len_B+1) for _ in range(len_A+1)]

for i in range(1, len_A+1):
    for j in range(1, len_B+1):
        # A[i] != B[j] 경우, 더 긴 쪽을 가지고 온다.
        if dp[i][j] < dp[i-1][j]:
            dp[i][j] = dp[i-1][j]
            path[i][j] = (i-1, j)
        
        if dp[i][j] < dp[i][j-1]:
            dp[i][j] = dp[i][j-1]
            path[i][j] = (i, j-1)
        
        # A[i] == B[j] 경우, 이전꺼에서 
        if A[i-1] == B[j-1] and dp[i][j] < dp[i-1][j-1] + 1 :
            dp[i][j] = dp[i-1][j-1] + 1
            path[i][j] = (i-1, j-1)


lcs = list()
i, j = len_A, len_B
while i > 0 and j > 0:
    if path[i][j] == (i-1, j-1) and A[i-1] == B[j-1]:
        lcs.append(A[i-1])
        i -= 1
        j -= 1
    else:
        i, j = path[i][j]

print("".join(reversed(lcs)))