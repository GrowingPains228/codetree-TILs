n = int(input())
arr = [0] + list(map(int, input().split()))
m = sum(arr)
dp = [False] * (m + 1)
dp[0] = True

ans = 0
for i in range(1,n+1):
    for j in range(m, -1, -1):
        if j >= arr[i] and dp[j - arr[i]]:
            dp[j] = True

            if j  == m-j :
                ans = max(ans, j)

print("Yes" if ans else "No")