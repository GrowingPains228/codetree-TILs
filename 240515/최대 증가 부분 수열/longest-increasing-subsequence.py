import sys

INT_MIN = -sys.maxsize
MAX_VALUE = 10000

n = int(input())
a = [0] + list(map(int, input().split()))
dp = [INT_MIN] * (MAX_VALUE + 1)

dp[0] = 0

for i in range(1,n+1):
    j = a[i]
    for l in range(a[i]):
        if dp[l] != INT_MIN:
            dp[j] = max(dp[j], dp[l]+1)

print(max(dp))