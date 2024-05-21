import sys

n = int(input())
arr = [0] + list(map(int, input().split()))
m = sum(arr)

dp = [0] * (m+1)
dp[0] = 1

# 일단 전체 합이 짝수 일때는 C에 아무것도 넣지 않거나 총합이 짝수 만큼 넣어야 하고
# 전체 합이 홀수 일대는 C에 홀수 합계 만큼 넣어 놓으면 된다.
# 최대한 적게 넣어야함.

# 일단 전체에서 C그룹에 하나씩 넣는다는 원리,

for i in range(1, n+1):
    for j in range(m, -1, -1):
        if j >= arr[i] and dp[j-arr[i]] != 0:
            dp[j] += 1

ans = 0
for i in range(n+1):
    for j in range(m, -1, -1):
        if j % 2 != 0:
            continue

        if j >= arr[i] and dp[j] and dp[j//2] >= 2:
            ans = max(ans, j//2)


print(ans)