n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

import sys
from sortedcontainers import SortedSet

# 비어 있는 의자들 세팅
s = SortedSet()
for i in range(1, m+1):
    s.add(i)

ans = 0
for elem in arr:
    chair = s.bisect_left(elem)
    if s[chair] == elem:
        s.remove(s[chair])
        ans += 1
    else:
        chair -= 1
        if chair < 0:
            print(ans)
            sys.exit()
        else:
            s.remove(s[chair])
            ans += 1

print(ans)