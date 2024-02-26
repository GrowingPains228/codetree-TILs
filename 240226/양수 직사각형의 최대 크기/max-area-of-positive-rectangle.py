n,m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def is_positive(x1, y1, x2, y2):
    return all([
        grid[i][j] > 0
        for i in range(x1, x2 + 1)
        for j in range(y1, y2 + 1)
    ])

def cal_Area(x1, y1, x2, y2):
    return (abs(x2-x1)+1)*(abs(y2-y1)+1)


ans = -1

for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                if is_positive(i, j, k, l) :
                    ans = max(ans, cal_Area(i, j, k, l))


print(ans)