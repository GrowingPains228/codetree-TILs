n,t = tuple(map(int, input().split()))

command_set = input()

arr = [
    list(map(int, input().split())) for _ in range(n)
]

def in_range(x,y) :
    return 0 <= x and x < n and 0 <= y and y < n

dxs, dys = [-1, 0, 1, 0],[0, 1, 0, -1]

x,y = n//2, n//2
direct = 0
ans = arr[x][y]
for i in range(t) :
    if command_set[i] == 'R' :
        direct = (direct + 1) % 4
    elif command_set[i] == 'L' :
        direct = (direct + 3) % 4
    else :
        nx, ny = x + dxs[direct], y + dys[direct]
        if in_range(nx,ny) :
            x ,y = x + dxs[direct], y + dys[direct]
            ans += arr[x][y]

print(ans)