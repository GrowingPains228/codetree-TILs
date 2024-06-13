import sys
from sortedcontainers import SortedSet
n, m = tuple(map(int, input().split()))
arr = SortedSet()
ans = sys.maxsize
for _ in range(n):
    num1 = int(input())
    arr.add(num1)

for i in range(n//2):
    num1 = arr[i]
    num2 = m + num1
    idx = arr.bisect_right(num2)
    if idx == len(arr):
        continue
    
    if arr[idx-1] == num2:
        ans = m
        break
    else:
        ans = min(ans, abs(arr[idx] - num1))

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)