import sys
INT_MAX = sys.maxsize

n = int(input())
arr = [0] + list(map(int, input().split()))
arr.sort()

# 일단 한 그룹에 전부 들어 있다고 가정하고, dp[0]를 계산한다.
# 그 다음, 원소들을 빼는 dp를 시행하면서
# 최소값을 찾는다.
# 여기서 dp 정의는,
m = sum(arr)
dp = [False] * (m + 1)
dp[0] = True

for i in range(1, n+1):
    for j in range(m, -1, -1):
        if arr[i] > j:
            continue

        if dp[j-arr[i]] == False:
            continue

        dp[j] = True

ans = INT_MAX
for i in range(1,m):
    if dp[i]:
        ans = min(ans, abs(i - (m - i)))

print(ans)