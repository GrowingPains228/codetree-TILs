n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

from sortedcontainers import SortedSet

# 비어 있는 의자들 세팅
s = SortedSet(range(1, m+1))

ans = 0
for elem in arr:
    chair = s.bisect_right(elem)
    if chair == 0:
        break

    s.remove(s[chair-1])
    ans += 1

print(ans)