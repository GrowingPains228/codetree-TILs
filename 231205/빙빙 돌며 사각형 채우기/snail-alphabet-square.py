n,m = tuple(map(int ,input().split()))

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
cur_dir = 0
arr = [
    [0]* m 
    for _ in range(n)
]
x,y = 0,0

def in_range(x,y) :
    return 0 <= x and x < n and 0 <= y and y < m

cnt_value = ord('A')
arr[x][y] = cnt_value
for i in range(1 , n * m) :
    nx, ny = x + dxs[cur_dir], y + dys[cur_dir]

    if not in_range(nx, ny) or arr[nx][ny] > 0 :
        cur_dir = (cur_dir + 1) % 4
    
    x,y = x + dxs[cur_dir], y + dys[cur_dir]
    
    cnt_value += 1

    if cnt_value == (ord('Z') + 1) :
        cnt_value = ord('A')

    arr[x][y] = cnt_value
    
for row in arr :
    for elem in row :
        print(chr(elem), end=" ")
    print()