from sortedcontainers import SortedSet

n, m = tuple(map(int, input().split()))

dots = [ tuple(map(int, input().split())) for _ in range(n) ]

s = SortedSet(dots)

for _ in range(m):
    k = int(input())
    idx = s.bisect_left((k,_))
    
    if idx == len(s):
        print(-1, -1)
    else:
        x,y = s[idx]
        print(x,y)
        s.remove(s[idx])