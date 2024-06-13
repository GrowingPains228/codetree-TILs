import sys
from sortedcontainers import SortedSet
n, m = tuple(map(int, input().split()))
arr = SortedSet()
ans = sys.maxsize
for _ in range(n):
    num1 = int(input())
    arr.add(num1)

for x in arr:
    min_idx = arr.bisect_left(m + x)
    if min_idx != len(arr):
        ans = min(ans, arr[min_idx] - x)
    
    # x 보다 m 이상 더 작으면서 가장 큰 값
    max_idx = arr.bisect_right(x - m) - 1
    if max_idx >= 0:
        ans = min(ans, x - arr[max_idx])

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)