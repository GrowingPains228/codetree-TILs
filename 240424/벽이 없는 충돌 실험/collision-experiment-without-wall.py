COORD_SIZE = 4000
OFFSET = 2000
BLANK = -1

#변수 선언 및 입력
t = int(input())
n = 0
marbles = []
next_marbles = []
next_marble_index = [
    [BLANK for _ in range(COORD_SIZE + 1)]
    for _ in range(COORD_SIZE + 1)
]

curr_time = 0
last_collision_time = -1

mapper = {
    'U' : 0,
    'R' : 1,
    'L' : 2,
    'D' : 3
}

def out_of_active_coordinate(marble):
    x, y, _, _, _ = marble
    return x < 0 or x > COORD_SIZE or y < 0 or y > COORD_SIZE


def move(marble):
    x, y, weight, move_dir, num = marble
    dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
    nx, ny = x + dxs[move_dir], y + dys[move_dir]

    return (nx, ny, weight, move_dir, num)


def find_duplicate_marble(marble):
    target_x, target_y, _, _, _ = marble
    return next_marble_index[target_x][target_y]


def collide(marble1, marble2):
    _, _, weight1, _, num1 = marble1
    _, _, weight2, _, num2 = marble2

    if weight1 > weight2 or (weight1 == weight2 and num1 > num2):
        return marble1
    else:
        return marble2


def push_next_marble(marble):
    global last_collision_time

    if out_of_active_coordinate(marble):
        return
    
    index = find_duplicate_marble(marble)

    if index == BLANK:
        next_marbles.append(marble)
        x, y, _, _, _ = marble
        next_marble_index[x][y] = len(next_marbles) - 1
    else :
        next_marbles[index] = collide(next_marbles[index], marble)
        last_collision_time = curr_time


def simulate():
    global marbles, next_marbles

    for marble in marbles:
        next_marble = move(marble)
        push_next_marble(next_marble)

    marbles = next_marbles[:]

    for x, y, _, _, _ in next_marbles:
        next_marble_index[x][y] = BLANK
    
    next_marbles = []



for _ in range(t):
    marbles = []
    last_collision_time = -1

    n = int(input())
    for i in range(1, n+1):
        x, y, weight, d = tuple(input().split())
        x, y, weight = int(x), int(y), int(weight)

        x, y = x*2, y*2
        x += OFFSET
        y += OFFSET
        marbles.append((x,y, weight, mapper[d], i))

    for i in range(1, COORD_SIZE +1) :
        curr_time = i
        simulate()

    print(last_collision_time)