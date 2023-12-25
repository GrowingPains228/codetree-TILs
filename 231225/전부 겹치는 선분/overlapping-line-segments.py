MAX_RANGE = 100
n = int(input())

max_x = MAX_RANGE
min_x = 0

for _ in range(n) :
    x1, x2 = tuple(map(int, input().split()))
    min_x = max(min_x, x1)
    max_x = min(max_x, x2)

if min_x > max_x :
    print("No")
else :
    print("Yes")