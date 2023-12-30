x1,y1, x2, y2 = tuple(map(int, input().split()))
a1,b1, a2, b2 = tuple(map(int, input().split()))

# 제일 왼쪽 하단 점
dx1, dy1 = (min(x1, a1), min(y1, b1))
# 제일 오른쪽 상단 점
dx2, dy2 = (max(x2, a2), max(y2, b2))

# 넓이
print((dx2- dx1)*(dy2-dy1))