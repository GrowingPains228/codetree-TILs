n, m = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))

# 지금까지 i번째 수까지만 고려해봤을 때,
# 고른 수의 합을 j로 만드는 것이 가능하면 True
# 불가능하면 False
# dp[i][j]
dp = [
    [False] * (m+1)
    for _ in range(n+1)
]

dp[0][0] = True

for i in range(1, n+1):
    for j in range(m+1):
        if j >= arr[i] and dp[i-1][j - arr[i]]:
            dp[i][j] = True
        
        if dp[i-1][j]:
            dp[i][j] = True
        

if dp[n][m]:
    print("Yes")
else:
    print("No")