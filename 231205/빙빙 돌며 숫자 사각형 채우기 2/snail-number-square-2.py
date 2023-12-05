n,m = tuple(map(int, input().split()))

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def in_range(x,y) :
    return 0 <= x and x < n and 0 <= y and y < m

dxs, dys = [1,0,-1,0],[0,1,0,-1]
x,y = 0,0
arr[0][0] = 1
direct = 0

for i in range(2,n*m + 1) :
    nx, ny = x + dxs[direct], y + dys[direct]
    if not in_range(nx, ny) or arr[nx][ny] > 0 :
        direct = (direct + 1) % 4

    x,y = x + dxs[direct], y + dys[direct]
    arr[x][y] = i

for row in arr :
    for elem in row :
        print(elem, end = " ")
    print()