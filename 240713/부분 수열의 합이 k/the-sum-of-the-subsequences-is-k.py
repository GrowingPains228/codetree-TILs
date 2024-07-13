n, k = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))

sumArr = [[0] * (n+1) for _ in range(n+1)]
ans = 0
for i in range(1, n+1):
    for j in range(i, n+1):
        sumArr[i][j] = sumArr[i][j-1] + arr[j]
        if sumArr[i][j] == k:
            ans += 1

print(ans)