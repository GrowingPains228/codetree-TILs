import sys
INT_MIN = -sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

ans = INT_MIN
for i in range(n-1) :
    for j in range(i+2, n) :
        ans = max(ans, arr[i] + arr[j])

print(ans)