n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

from sortedcontainers import SortedSet

# 비어 있는 의자들 세팅
s = SortedSet()
for i in range(1, m+1):
    s.add(i)

ans = 0
for elem in arr:
    chair = s.bisect_right(elem)
    if len(s) == 0 or chair - 1 < 0:
        break
    else :
        s.remove(s[chair-1])
        ans += 1

print(ans)