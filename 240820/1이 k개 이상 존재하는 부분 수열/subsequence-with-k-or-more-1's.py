import sys
n ,k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

j = 0
countingCnt = 0
ans = sys.maxsize
for i in range(1, n+1):
    while j+1 <= n and countingCnt < k:
        if arr[j+1] == 1:
            countingCnt += 1
        j += 1

    if countingCnt >= k:
        ans = min(ans, j - i + 1)

    if arr[i] == 1:
        countingCnt -= 1

print(ans)