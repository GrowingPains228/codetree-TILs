n = int(input())

def in_range(x, y) :
    global n
    return 0 <= x and x < n and 0 <= y and y < n

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]


a = [
    list(map(int, input().split()))
    for _ in range(n)
]
x,y = 0,0

ans = 0
for i in range(n) :
    for j in range(n) :
        y = i
        x = j
        cnt = 0
        for dx, dy in zip(dxs, dys) :
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and a[nx][ny] >= 1 :
                cnt += 1

        if cnt >= 3 :
            ans += 1

print(ans)