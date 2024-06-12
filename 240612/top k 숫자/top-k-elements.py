n, k = tuple(map(int, input().split()))

from sortedcontainers import SortedSet
s = SortedSet()
arr = list(map(int, input().split()))
for elem in arr:
    s.add(elem)

for i in range(1, k+1):
    print(s[-i], end = " ")