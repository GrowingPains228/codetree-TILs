import sys
MAX_RANGE = 100
n = int(input())

lines = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

tf = False
for i in range(n) :
    max_x1 = 1
    min_x2 = MAX_RANGE
    for j in range(n) :
        if i == j :
            continue
        
        x1, x2 = lines[j]
        max_x1 = max(max_x1, x1)
        min_x2 = min(min_x2, x2)

    if max_x1 <= min_x2 :
        tf = True
        break

print("Yes" if tf else "No")