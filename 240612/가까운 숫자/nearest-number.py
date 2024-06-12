import sys
from sortedcontainers import SortedSet
n = int(input())
s = SortedSet()
s.add(0)
dots = list(map(int, input().split()))
ans = sys.maxsize

for dot in dots:
    if s.bisect_right(dot) == len(s):
        ans = min(ans, dot - s[s.bisect_right(dot)-1])
    else:
        ans = min(ans, dot - s[s.bisect_right(dot)-1], s[s.bisect_right(dot)] - dot)
    
    s.add(dot)
    print(ans)