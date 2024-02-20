MAX_LENGTH = 100
memory_arr = [0] * (MAX_LENGTH + 1)
n,m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
cnt_happyArr = 0
# 가로 체크
for i in range(n) :
    row = False
    height = False
    for j in range(n) :
        if j + m -1 >= n or (row and height):
            break
        
        if not row :
            for k in range(m) :
                if grid[i][j] != grid[i][j + k]:
                    row = False
                    break

                row = True
            
            cnt_happyArr += 1 if row else 0
        
        if not height :
            for k in range(m) :
                if grid[j][i] != grid[j + k][i]:
                    height = False
                    break
            
                height = True

            cnt_happyArr += 1 if height else 0

print(cnt_happyArr)