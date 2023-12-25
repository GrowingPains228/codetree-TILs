MAX_RANGE = 100
n = int(input())

max_x1 = 0
min_x2 = MAX_RANGE
cnt = 0
for _ in range(n) :
    x1, x2 = tuple(map(int, input().split()))
    if x1 > min_x2 or x2 < max_x1 :
        continue
    
    max_x1 = max(max_x1, x1)
    min_x2 = min(min_x2, x2)
    cnt += 1

print("Yes" if cnt == n-1 or cnt == 1 else "No")