n = int(input())
arr = list(map(int, input().split()))
dp = [0]*n


def initialize():
    for i in range(n):
        dp[i] = 0
    
    dp[0] = 1


initialize()
for i in range(1,n):
    dp[i] = 1
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))