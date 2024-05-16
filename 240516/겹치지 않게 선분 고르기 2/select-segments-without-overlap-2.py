MAX_INT = 1000
n = int(input())
line_group = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
line_group.sort()

# 시간 복잡도 N^2 으로 끝내야 한다.
dp = [0]*n
dp[0] = 1

for i in range(1, n):
    x1, x2 = line_group[i]
    dp[i] = 1
    for j in range(i):
        x3, x4 = line_group[j]
        if x2 < x3 or x4 < x1: # any([element for i in range(]
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))