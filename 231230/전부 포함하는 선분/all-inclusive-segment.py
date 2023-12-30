import sys
MAX_INT = sys.maxsize
n = int(input())

line_group = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# 선분 하나를 제외시킨 완전탐색을 실행
ans = MAX_INT
for i in range(n) :
    min_x, max_x = MAX_INT,0
    for j in range(n) :
        if i == j :
            continue
        x1,x2 = line_group[j]

        min_x = min(min_x, x1)
        max_x = max(max_x, x2)
    
    ans = min(ans , max_x- min_x)

print(ans)