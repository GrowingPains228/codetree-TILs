n = int(input())
arr = [
    [0] * n
    for _ in range(n)
]

def in_range(x,y) :
    return 0 <= x and x < n and 0 <= y and y < n

dxs, dys = [0,-1,0,1],[-1,0,1,0]
cur_dir = 0
x,y = n -1, n -1
arr[x][y] = n ** 2
for i in range(n**2 -1,0, -1) :
    nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
    if not in_range(nx, ny) or arr[nx][ny] > 0 :
        cur_dir = (cur_dir + 1) % 4
    
    x, y = x + dxs[cur_dir], y + dys[cur_dir]
    arr[x][y] = i

for row in arr :
    for elem in row :
        print(elem, end = " ")
    print()