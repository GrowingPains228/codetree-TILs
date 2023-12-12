import sys
INT_MAX = sys.maxsize
MAX_RANGE = 40001
n = int(input())
segments = [
    tuple(map(int, input().split())) for _ in range(n)
]

min_area = INT_MAX
for i in range(n) : 
    area = 0
    min_x, max_x = MAX_RANGE,-1
    min_y, max_y = MAX_RANGE,-1
    for j in range(n) :
        if i == j :
            continue
        
        x, y = segments[j]

        # 점들을 추출해서 원점과 가장 멀리있는 점과, 가장 가까 이 있는 점을 기록한다.
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    area = (max_x - min_x)*(max_y - min_y)
    min_area = min(min_area, area)

print(min_area)