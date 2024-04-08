n, m, r, c = tuple(map(int, input().split()))
r,c = r-1, c-1
grid = [[0]*n for _ in  range(n)]
grid[r][c] = 1
c_grid = [[0]*n for _ in range(n)]


def In_Range(r,c) :
    return r >= 0 and r < n and c >= 0 and c < n


def Is_Bomb(r,c) :
    return grid[r][c]


def Bomb_Func(r, c, t) :
    global grid, c_grid
    dr_arr, dc_arr = [-1, 0, 1, 0], [0, 1, 0, -1]
    for dr, dc in zip(dr_arr, dc_arr):
        xr, xc = r + dr*(2**(t-1)), c + dc*(2**(t-1))
        if In_Range(xr, xc):
            c_grid[xr][xc] = 1

for t in range(1, m+1):
    c_grid = [arr[:] for arr in grid]
    for i in range(n) :
        for j in range(n):
            if Is_Bomb(i, j):
                Bomb_Func(i, j, t)
    grid = [arr[:] for arr in c_grid]

ans = 0
for row in grid:
    for elem in row:
        if elem :
            ans += 1

print(ans)