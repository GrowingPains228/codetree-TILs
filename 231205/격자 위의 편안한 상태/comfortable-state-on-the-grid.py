n,m = tuple(map(int, input().split()))

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x,y) :
    return 0 <= x and x < n and 0 <= y and y < n

def is_Comfortable(x,y) :
    cnt = 0
    for dx, dy in zip(dxs, dys) :
        xn,yn = x + dx, y + dy

        if in_range(xn, yn) and arr[xn][yn] != 0 :
            cnt += 1

    return cnt == 3
            
def Coloring(x,y) :
    if in_range(x,y) and arr[x][y] == 0 :
        arr[x][y] = 1


for _ in range(m) :
    x,y = tuple(map(int, input().split()))
    Coloring(x-1,y-1)
    print(1 if is_Comfortable(x-1,y-1) else 0)