MAX_VALUE = 10001
n, m = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))

dp = [0]*(m+1)


def initialize():
    for i in range(m+1):
        dp[i] = MAX_VALUE
    
    dp[0] = 0


initialize()

for i in range(1, n+1):
    for j in range(m, -1, -1):
        if j >= arr[i]:
            if dp[j - arr[i]] == MAX_VALUE:
                continue
            
            dp[j] = min(dp[j], dp[j - arr[i]] + 1)

if dp[m] == MAX_VALUE:
    print(-1)
else :
    print(dp[m])