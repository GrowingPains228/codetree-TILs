n = int(input())

x,y = 0,0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for _ in range(n) :
    move, distance = tuple(input().split())
    distance = int(distance)
    if move == 'W' :
        x,y = x + distance*dx[0], y + distance*dy[0]
    elif move == 'S' :
        x,y = x + distance*dx[1], y + distance*dy[1]
    elif move == 'N' :
        x,y = x + distance*dx[2], y + distance*dy[2]
    else  :
        x,y = x + distance*dx[3], y + distance*dy[3]

print(x,y)