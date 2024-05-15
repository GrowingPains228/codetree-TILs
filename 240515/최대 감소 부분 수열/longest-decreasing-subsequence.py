import sys
INT_MIN = -sys.maxsize
MAX_VALUE = 10000

n = int(input())
arr = [MAX_VALUE+1] + list(map(int, input().split()))
dp = [INT_MIN] * (MAX_VALUE+2)
dp[MAX_VALUE+1] = 0
for i in range(1, n+1):
    j = arr[i]

    for l in range(MAX_VALUE+1, j, -1):
        if dp[l] == INT_MIN:
            continue
        
        dp[j] = max(dp[j], dp[l]+1)


print(max(dp))