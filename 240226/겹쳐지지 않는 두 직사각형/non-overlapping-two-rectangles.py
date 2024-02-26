import sys
MIN_INT = -sys.maxsize

n,m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x,y) :
    return x >= 0 and x < n and y >= 0 and y < m

def is_Overlap(x1, y1, x2, y2, h1, w1, h2, w2):
    for x in range(x2, x2 + h2) :
        for y in range(y2, y2 + w2) :
            if x >= x1 and x < x1 + h1 and y >= y1 and y < y1 + w1 :
                return True

    return False


def get_maxScore(x, y, height, width) :
    return sum([
        grid[i][j]
        for i in range(x, x + height)
        for j in range(y, y + width)
    ])

ans = MIN_INT
# 왼쪽 제일 위의 좌표를 잡아주고
for x1 in range(n) :
    for y1 in range(m) :
        for h1 in range(1, n+1) :
            for w1 in range(1, m+1) :
                if in_range(x1 + h1 - 1, y1 + w1 - 1) :
                    for x2 in range(n) :
                        for y2 in range(m) :
                            for h2 in range(1, n+1) :
                                    for w2 in range(1,m+1) :
                                        if not in_range(x2 + h2 - 1, y2 + w2 - 1) :
                                            continue

                                        if is_Overlap(x1, y1, x2, y2, h1, w1, h2, w2) :
                                            continue

                                        ans = max(ans, get_maxScore(x1, y1, h1, w1) + get_maxScore(x2, y2, h2, w2))

print(ans)