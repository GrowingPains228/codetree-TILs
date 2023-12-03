def Return_Direction_Type(direction) :
    if direction == 'N' :
        return 0
    elif direction == 'E' :
        return 1
    elif direction == 'S' :
        return 2
    else : # direction == 'W'
        return 3


n = int(input())
x,y = 0,0

# 0 : N/ 1 : E/ 2 : S/ 3 : W
dx,dy = [0, 1, 0, -1], [1, 0, -1, 0]

for _ in range(n) :
    direction, m = tuple(input().split())
    d = Return_Direction_Type(direction)
    m = int(m)

    x += dx[d] * m
    y += dy[d] * m

print(x,y)