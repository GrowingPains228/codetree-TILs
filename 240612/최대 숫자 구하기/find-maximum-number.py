from sortedcontainers import SortedSet

n,m = tuple(map(int, input().split()))
balls = [ i for i in range(1, m+1)]
s = SortedSet()
for ball in balls:
    s.add(ball)
inp = list(map(int, input().split()))

for elem in inp:
    s.remove(elem)
    print(s[-1])