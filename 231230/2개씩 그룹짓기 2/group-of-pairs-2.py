import sys
MAX_INT = sys.maxsize
n = int(input())
arr = list(map(int, input().split()))

arr.sort()
ans = MAX_INT
for i in range(n) :
    ans = min(ans, arr[i + n] - arr[i])

print(ans)