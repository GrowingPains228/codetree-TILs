n, t = tuple(map(int, input().split()))

def in_range(x, y) : 
    return 0 <= x and x < n and 0 <= y and y < n

dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]

direct = {
    'U' : 0,
    'R' : 1,
    'L' : 2,
    'D' : 3
}

r, c, d = tuple(input().split())

d_type = direct[d]
r,c = int(r), int(c)
x,y = r-1, c-1

for _ in range(t) :
    if in_range(x + dxs[d_type], y + dys[d_type]) :
        x,y = x + dxs[d_type], y + dys[d_type]
    else :
        d_type = 3 - d_type
    

print(x + 1,y + 1)