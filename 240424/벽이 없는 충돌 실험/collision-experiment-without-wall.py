COORD_SIZE = 4000
OFFSET = 2000
BLANK = -1

# 변수 선언 및 입력
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

# 해당 구슬이 1초 후에 어느 위치에 있는지를 구해 상태를 반환한다.
def move(marble):
    dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

    x, y, weight, move_dir, num = marble
    nx, ny = x + dxs[move_dir], y + dys[move_dir]

    return (nx, ny, weight, move_dir, num)


# 해당 구슬이 충돌이 일어나는 구슬이 있는지 확인한다. 
def find_duplicate_marble(marble):
    target_x, target_y, _, _, _ = marble

    return next_marble_index[target_x][target_y]


# 두 구슬이 같은 위치에서 충돌했을 경우 
# 살아남는 구슬을 반환한다.
def collide(marble1, marble2):
    _, _, weight1, _, num1 = marble1
    _, _, weight2, _, num2 = marble2

    # 첫 번째 구슬이 살아남게 되는 경우는
    # 첫 번째 구슬의 무게가 더 크거나
    # 무게는 같은데 번호가 더 클 경우 이다.
    if weight1 > weight2 or (weight1 == weight2 and num1 > num2):
        return marble1
    else:
        return marble2

# 구슬이 이미 (0,0) ~ (COORD_SIZE, COORD_SIZE) 사이를 벗어나
# 더 이상 충돌이 일어나지 않으므로
# Active Coordinate를 벗어났다고 판단한다.
def out_of_active_coordinate(marble):
    x, y, _, _, _ = marble
    return x < 0 or x > COORD_SIZE or y < 0 or y > COORD_SIZE


# 다음 구슬의 목록에 반영
def push_next_marble(marble):
    global last_collision_time

    # 볼 필요 없는 구슬은 더이상 계산하지 않음.
    if out_of_active_coordinate(marble) :
        return

    index = find_duplicate_marble(marble)

    # Case1 : 같은 위치에 있는 구슬이 아직 없다면 그대로 목록에 추가
    if index == BLANK:
        next_marbles.append(marble)

        x, y, _, _, _ = marble
        next_marble_index[x][y] = len(next_marbles) - 1
    
    # Case 2 : 다음 구슬의 목록 중 같은 위치에 구슬이 이미 있다면
    # 더 영향력 있는 구슬만 남기고
    # 현재 시간을 가장 최근 충돌 시간에 기록한다.
    else : 
        next_marbles[index] = collide(next_marbles[index], marble)
        last_collision_time = curr_time



def simulate():
    global marbles, next_marbles

    for marble in marbles:
        #Step1. 각 구슬에 대해 한 칸 움직인 이후의 위치를 받아온다.
        next_marble = move(marble)

        #Step2. 그 다음 구슬의 목록에 반영한다.
        push_next_marble(next_marble)

    marbles = next_marbles[:]


    for x, y, _, _, _ in next_marbles:
        next_marble_index[x][y] = BLANK


    #그 다음 simultation 때 다시 사용해야 하므로
    # 구슬의 목록 을 미리 초기화 해준다.
    next_marbles = []


for _ in range(t):
    # 새로운 테스트 케이스가 시작 될때마다 기존에 사용하던 값들을 초기화해준다.
    marbles = []
    last_collision_time = -1

    # 입력
    n = int(input())
    for i in range(1, n + 1):
        x,y,weight,d = tuple(input().split())
        x, y, weight = int(x), int(y), int(weight)

        # 구슬이 움직이는 도중에 충돌하는 문제를 깔끔하게 처리하기 위해
        # 좌표를 2배로 불려 1초에 한칸 씩 이동하는 문제로 바꾼다.
        # 이렇게 문제가 바뀌면 따로 구슬이 움직이는 도중 충돌하는 경우를 생각하지 않아도 된다.
        x,y = x * 2, y*2

        #좌표를 전부 양수로 만들어야 동일한 위치에서 충돌이 일어나는지를
        # 판단하는 데 사용할 next_marble_index 배열에
        # 각 구슬의 위치마다 자신의 index를 저장할 수 있으므로
        # 좌표를 전부 양수로 만든다.
        # 입력으로 들어올 수 있는 좌표값 중 가장 작은 값이 -2000 이므로
        # OFFSET을 2000으로 잡아 전부 더해준다.
        # 같은 OFFSET을 모든 구슬에 전부 더해주는 것은
        # 답에 전혀 영향을 미치지 않는다.
        x += OFFSET; y += OFFSET;
        marbles.append((x,y,weight,mapper[d],i))

    # 처음에 구슬들은 전부
    # (-2000, -2000)에서 (2000, 2000) 사이에 있기 때문에
    # COORD SIZE + 1 (4001)만큼 이동하면
    # 입력으로 주어진 구슬들이 모두 (-2000, -2000) ~ (2000, 2000)
    # 영역 밖으로 벗어나게 되므로 더 이상 충돌이 일어나지 않게 됩니다.
    # 따라서 시뮬레이션을 총 COORD_SIZE번 진행합니다.
    for i in range(1, COORD_SIZE + 1):
        curr_time = i
        simulate()

    print(last_collision_time)