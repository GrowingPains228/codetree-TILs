MAP_RANGE = 100

n, k = tuple(map(int, input().split()))
myMap = [[0] * (n+1)] + [([0] + list(map(int, input().split()))) for _ in range(n)]

sumArr = [[0] * (n+1) for _ in range(n+1)]
ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        sumArr[i][j] = myMap[i][j] + sumArr[i-1][j] + sumArr[i][j-1] - sumArr[i-1][j-1]

        if i-k < 1 or j - k < 1:
            continue
            
        ans = max(ans, sumArr[i][j] - sumArr[i-k][j] - sumArr[i][j-k] + sumArr[i-k][j-k])

print(ans)