n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 제일 위에서, index_row = 0 에서, (0,1) , (0,2), (0,3) 구간이 가장 큰 값이 나올것!
# 벽면까지 이동하면 됨.

# 직사각형을 이루는 지점에 적힌 숫자들의 합이 최대가 되도록 하는거면,
# 굳이 반드시 밑에서 출발해서 반시계로 돌 필요가 있을까..?
# 일단 하라는 대로 해보기.
def in_range(x,y) :
    return x >= 0 and x < n and y >= 0 and y < n

def get_score(x, y, k, l) :
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    move_nums = [k, l, k, l]

    sum_of_nums = 0
    
    for dx, dy, move_num in zip(dxs, dys, move_nums) :
        for _ in range(move_num) :
            x, y = x + dx, y + dy

            if not in_range(x,y) :
                return 0
            
            sum_of_nums += grid[x][y]

    return sum_of_nums


# (3,2) 에서부터 시작이 가능하다!
# 모든 
ans = 0
for i in range(2,n) :
    for j in range(1,n-1) :
        for k in range(1,n) :
            for l in range(1,n) :
                ans = max(ans, get_score(i, j, k, l))

print(ans)