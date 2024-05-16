n = int(input())
arr = list(map(int, input().split()))

dp = [1]* (n)

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

arr = arr[::-1]
dp_re = [1]* (n)
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_re[i] = max(dp_re[i], dp_re[j] + 1)

dp_re.reverse()
ans = 0
for i in range(n):
    ans = max(ans, dp[i] + dp_re[i] - 1)

print(ans)