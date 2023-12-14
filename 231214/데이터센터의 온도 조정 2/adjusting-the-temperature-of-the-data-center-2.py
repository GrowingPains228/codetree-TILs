import sys
MAX_INT = sys.maxsize
MIN_INT = -sys.maxsize

n,c,g,h = tuple(map(int, input().split()))

n_T = []

min_t = MAX_INT
max_t = MIN_INT

for _ in range(n) :
    (Ta, Tb) = tuple(map(int, input().split()))
    min_t = min(min_t, Ta)
    max_t = max(max_t, Tb)
    n_T.append((Ta, Tb))

def check(machine, T) :
    Ta, Tb = n_T[machine]

    if Ta > T :
        return c
    elif Tb >= T :
        return g
    else :
        return h

ans = 0
for t in range(min_t-1, max_t +2) :
    t_value = 0
    for i in range(n) :
        t_value += check(i,t)
    ans = max(ans, t_value)

print(ans)