import sys
MAX_VALUE = 1000
MAX_N = 100
INT_MAX = MAX_VALUE * MAX_N + 1

n = int(input())
arr = [0] + list(map(int, input().split()))
arr.sort()

# 일단 한 그룹에 전부 들어 있다고 가정하고, dp[0]를 계산한다.
# 그 다음, 원소들을 빼는 dp를 시행하면서
# 최소값을 찾는다.
# 여기서 dp 정의는,
# 
dp = [INT_MAX] * (MAX_VALUE * MAX_N + 1)
dp[0] = sum(arr)

for i in range(1, n+1):
    for j in range(MAX_VALUE * MAX_N, -1, -1):
        if arr[i] > j:
            continue
        
        if dp[j - arr[i]] == INT_MAX:
            continue
        
        dp[j] = min(dp[j],abs(dp[j - arr[i]] - 2*arr[i]))

print(min(dp[1::]))