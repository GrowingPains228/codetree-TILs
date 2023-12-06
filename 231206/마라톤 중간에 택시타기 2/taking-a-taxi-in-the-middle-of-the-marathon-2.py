import sys
INT_MAX = sys.maxsize

n = int(input())
check_po = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = INT_MAX
for i in range(1, n - 1) :
    temp_root = check_po[:i] + check_po[i + 1 :]
    distance = 0
    for j in range(1, len(temp_root)) :
        x1, y1 = temp_root[j - 1]
        x2, y2 = temp_root[j]
        distance += abs(x1 - x2) + abs(y1 - y2)
        
    ans = min(ans, distance)

print(ans)