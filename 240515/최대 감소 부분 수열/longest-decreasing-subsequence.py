INT_MIN = -1
MAX_VALUE = 10000

n = int(input())
arr = [MAX_VALUE+1] + list(map(int, input().split()))
dp = [0]* (n+1)

for i in range(n+1):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))