import sys
MAX_VALUE = -1
n,m  = tuple(map(int,input().split()))
arr = [0]+ list(map(int,input().split()))
dp=[0]*(m+1)

def initialize():
    for i in range(m+1):
        dp[i] = MAX_VALUE

    dp[0] = 0


initialize()
for i in range(1, m+1):
    for j in range(n+1):
        if i >= arr[j]:
            if dp[i-arr[j]] == MAX_VALUE:
                continue

            dp[i]=max(dp[i],dp[i-arr[j]]+1)
if dp[m]==MAX_VALUE:
    print(-1)
else :
    print(dp[m])