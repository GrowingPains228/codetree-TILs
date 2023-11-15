n = int(input())

x,y = 0,0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for _ in range(n) :
    move, distance = tuple(input().split())
    distance = int(distance)
    if move == 'W' :
        move_dir = 0
    elif move == 'S' :
        move_dir = 1
    elif move == 'N' :
        move_dir = 2
    else  :
        move_dir = 3

    x,y = x + distance*dx[move_dir], y + distance*dy[move_dir]

print(x,y)