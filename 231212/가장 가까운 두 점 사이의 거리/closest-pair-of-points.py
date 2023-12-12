import sys
INT_MAX = sys.maxsize
n = int(input())
segments = [
    tuple(map(int, input().split())) for _ in range(n)
]

min_distance = INT_MAX
for i in range(n) :
    for j in range(i + 1, n) :
        x1, y1 = segments[i]
        x2, y2 = segments[j]
        distance = (x2-x1)**2 + (y2-y1)**2
        min_distance = min(min_distance, distance)

print(min_distance)