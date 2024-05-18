import sys
MAX_VALUE = 10000

n, m = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))
arr.sort()

if sum(arr) < m or min(arr) > m:
    print("No")
    sys.exit()

dp = [-1] * (MAX_VALUE+1)
dp[0] = 0


for i in range(1, n+1):
    for j in range(MAX_VALUE, -1, -1):
        if j < arr[i]:
            continue
        
        if dp[j - arr[i]] == -1:
            continue
        
        dp[j] = 1


if dp[m] == -1:
    print("No")
else:
    print("Yes")