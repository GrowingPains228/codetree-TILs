import sys
MAX_VALUE = 10000

n, m = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))

if sum(arr) < m or min(arr) > m:
    print("No")
    sys.exit()

dp = [-1] * (MAX_VALUE+1)
dp[0] = 0


for i in range(1, m+1):
    for j in range(n+1):
        if i < arr[j]:
            continue

        if dp[i - arr[j]] == -1:
            continue
        
        dp[i] = dp[i - arr[j]] + 1

if dp[m] == -1:
    print("No")
else:
    print("Yes")