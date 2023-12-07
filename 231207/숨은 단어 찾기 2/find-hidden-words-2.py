n,m = tuple(map(int, input().split()))
arr = [input() for _ in range(n)]

def in_range(x,y) :
    return 0 <= x and x < n and 0 <= y and y < m

dxs, dys = [1, 1, 0, -1, -1, -1, 0, 1], [0, -1, -1, -1, 0, 1, 1, 1]

cnt = 0
for i in range(n):
    for j in range(m) :
        if arr[i][j] != 'L' :
            continue

        x = i
        y = j
        for dx,dy in zip(dxs, dys) :
            count = 0
            nx, ny = x + dx, y + dy
            while in_range(nx, ny) and arr[nx][ny] == 'E':
                nx,ny = nx + dx, ny + dy
                count += 1

                if count == 2 :
                    cnt += 1
                    break


print(cnt)