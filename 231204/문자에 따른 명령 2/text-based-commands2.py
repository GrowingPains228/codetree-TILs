dx,dy = [0, 1, 0, -1], [1, 0 , -1, 0]

direction = 0  #북쪽 방향
x,y = 0,0

comman = list(input())

for elem in comman :
    if elem == 'F' :
        x,y = x + dx[direction], y + dy[direction]
    elif elem == 'R' :
        direction = (direction + 1) % 4
    else : #'L' 일때
        direction = (direction + 3) % 4

print(x,y)