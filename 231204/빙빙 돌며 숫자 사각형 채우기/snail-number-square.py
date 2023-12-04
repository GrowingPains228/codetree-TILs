n, m = tuple(map(int, input().split()))

def in_range(x,y) :
    return 0 <= x and x < n and 0 <= y and y < m

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

direct_num = 0

x,y = 0,0
arr[0][0] = 1

for i in range(2, n * m + 1) :
    nx, ny = x + dxs[direct_num], y + dys[direct_num]

    if not in_range(nx, ny) or arr[nx][ny] != 0 :
        direct_num = (direct_num + 1) % 4

    x, y = x + dxs[direct_num], y + dys[direct_num]
    arr[x][y] = i

for row in arr :
    for elem in row :
        print(elem, end = " ")
    print()