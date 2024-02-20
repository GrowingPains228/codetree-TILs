n,m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def is_in_range(x,y, block) :
    for elem in block :
        dx, dy = elem
        rx, ry = x + dx, y + dy
        if rx >= m or rx < 0 or ry >= n or ry < 0 :
            return False
    
    return True
        
# 첫번째 블록 + 두번째 블록
type_shape = [[(0,0), (0,1), (1,1)], 
                [(0,0),(1,0),(1,1)],
                [(0,0), (0,1), (-1,1)],
                [(0,0),(-1,0),(-1,1)],
                [(0,0), (1,0), (2,0)],
                [(0,0), (0,1),(0,2)]]

max_sum = 0
for i in range(n) :
    for j in range(m) :
        # 첫번째 블럭
        for block in type_shape :
            if not is_in_range(j,i, block) : # 범위안에 포함되어있지 않다면, 
                continue                         # 패스
            
            sum_num = 0
            for elem in block :
                dx, dy = elem
                sum_num += grid[i+dy][j+dx]

            max_sum = max(max_sum, sum_num)
        
print(max_sum)