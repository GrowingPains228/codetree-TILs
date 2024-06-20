from sortedcontainers import SortedSet

n,m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
s = SortedSet()

for i in range(1, m+1):
    s.add(i)

ans = 0
for elem in arr:
    idx = s.bisect_right(elem)

    if idx -1 < 0:
        break
    else:
        ans += 1
        s.remove(s[idx-1])
    

print(ans)