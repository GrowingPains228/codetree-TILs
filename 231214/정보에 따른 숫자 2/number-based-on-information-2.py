import sys

INT_MAX = sys.maxsize

T, a, b = tuple(map(int, input().split()))

arr = [
    tuple(input().split())
    for _ in range(T)
]

ans = 0
for i in range(a,b+1) :

    distance_s = INT_MAX
    distance_n = INT_MAX

    for (alpha, idx) in arr :
        idx = int(idx)

        if alpha == 'S' :
            distance_s = min(distance_s, abs(i-idx))
        else :
            distance_n = min(distance_n, abs(i-idx))

    if distance_s <= distance_n :
        ans += 1

print(ans)