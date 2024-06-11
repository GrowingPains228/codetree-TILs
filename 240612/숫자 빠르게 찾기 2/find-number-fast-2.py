n, m = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

from sortedcontainers import SortedSet
s = SortedSet()

for elem in arr:
    s.add(elem)

for _ in range(m):
    target = int(input())
    if s.bisect_left(target) == len(s):
        print(-1)
    else:
        print(s[s.bisect_left(target)])