n,t = tuple(map(int, input().split()))

dxs, dys = [1, 0, 0, -1], [0, 1, -1, 0]

def in_range(nx, ny) :
    return 0 <= nx and nx < n and 0 <= ny and ny <= n

direct = {
    'U' : 0,
    'D' : 3,
    'R' : 1,
    'L' : 2
}

r, c, d = tuple(input().split())

x,y = int(r) -1, int(c) -1
cur_d = direct[d]

for _ in range(t) :
    if not in_range(x + dxs[cur_d], y + dys[cur_d]) :
        cur_d = 3 - cur_d
    else :
        x, y = x + dxs[cur_d], y + dys[cur_d]


print(x + 1, y + 1)