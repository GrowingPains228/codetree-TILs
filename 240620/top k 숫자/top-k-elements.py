from sortedcontainers import SortedSet

s = SortedSet()
n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

for elem in arr:
    s.add(-elem)

for i in range(k):
    print(-s[i], end = " ")