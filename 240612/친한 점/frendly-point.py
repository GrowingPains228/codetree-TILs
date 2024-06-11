from sortedcontainers import SortedSet
n, m = tuple(map(int, input().split()))

dot_arr = SortedSet()
for _ in range(n):
    x,y = tuple(map(int, input().split()))
    dot_arr.add((x,y))

for _ in range(m):
    x,y = tuple(map(int, input().split()))
    if dot_arr.bisect_left((x,y)) == len(dot_arr):
        print(-1, -1)
    else:
        a,b = dot_arr[dot_arr.bisect_left((x, y))]
        print(a, b)