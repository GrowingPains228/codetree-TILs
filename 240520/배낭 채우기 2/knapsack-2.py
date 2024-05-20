import sys
INT_MIN = -sys.maxsize

n,m = tuple(map(int, input().split()))
jewels = list()
for _ in range(n):
    weight, value = tuple(map(int, input().split()))
    jewels.append((weight, value))

dp = [INT_MIN] * (m+1)
dp[0] = 0
for (weight, value) in jewels:
    for j in range(1, m+1):
        if weight <= j and dp[j-weight] != INT_MIN:
            dp[j] = max(dp[j], dp[j-weight] + value)
        
print(max(dp))