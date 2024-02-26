n,m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def is_positive(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if grid[i][j] <= 0 :
                return False
    return True


def cal_Area(x1, y1, x2, y2):
    return (abs(x2-x1)+1)*(abs(y2-y1)+1)


def find_rect():
    max_area = -1
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if is_positive(i, j, k, l) :
                        max_area = max(max_area, cal_Area(i, j, k, l))
    return max_area


ans = -1
ans = find_rect()
print(ans if ans > 0 else -1)