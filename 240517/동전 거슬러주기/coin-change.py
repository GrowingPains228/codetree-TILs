import sys
MAX_INT = sys.maxsize
MAX_VALUE = 10000

n, m = map(int, input().split())
coins = [0] + list(map(int, input().split()))
dp = [0]*(m+1)


def initialize():
    for i in range(1, m+1):
        dp[i] = MAX_INT
    
    dp[0] = 0


initialize()
for i in range(1, m + 1):
    for j in range(1,n+1):
        if  i < coins[j]:
            continue
        
        dp[i] = min(dp[i], dp[i - coins[j]] + 1)

print(dp[m])