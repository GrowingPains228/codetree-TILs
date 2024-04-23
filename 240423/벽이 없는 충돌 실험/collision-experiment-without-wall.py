MAX_RANGE = 1000
TEST_CASE = int(input())
ans = []
beads = []
next_beads = []

def In_Range(x,y):
    return 0 <= x and x < 2*MAX_RANGE and 0 <= y and y < 2*MAX_RANGE


# 튕기는 경우도 없고, 떨어지는 경우도 고려 안해도됨.
# 계속 굴러 간다는 의미!
def Get_NextPos(x, y, d):
    dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
    nx, ny = x + dxs[d], y + dys[d]

    return (nx, ny)


def Move_all():
    for x in range(2*MAX_RANGE + 1):
        for y in range(2*MAX_RANGE + 1):
            for (w, num, d) in beads[x][y]:
                (next_x, next_y) = Get_NextPos(x,y, d)

                if not In_Range(next_x, next_y):
                    next_beads[x][y].append(w, num, d)
                else:
                    next_beads[next_x][next_y].append(w, num, d)


def Selected_marble():
    tf = False
    for x in range(2*MAX_RANGE + 1):
        for y in range(2*MAX_RANGE + 1):
            if len(next_beads[x][y]) > 2:
                next_beads[x][y].sort(key = lambda x : (-x[0], -x[1]))

                while len(next_beads[x][y]) > 2:
                    next_beads[x][y].pop()
                    tf = True
    return tf

def Simulateion(time):
    conflic_time = -1
    for t in range(1, time+1):
        IsConflict = False
        next_beads = [
            [[]for _ in range(2 * MAX_RANGE + 1)]
            for _ in range(2 * MAX_RANGE + 1)
        ]

        # 모든 구슬을 움직여 준다.
        Move_all()

        # 모든 구슬 중 충돌이 있었는지 검사하면서 충돌 제거
        IsConflict = Selected_marble()

        for i in range(n):
            for j in range(n):
                beads[i][j] = next_beads[i][j]
        if IsConflict:
            conflic_time = t
    return conflic_time


dir_mapper = {
    'U' : 0,
    'R' : 1,
    'L' : 2,
    'D' : 3
}

for _ in range(TEST_CASE):
    n = int(input())
    beads = [
        [[]for _ in range(2 * MAX_RANGE + 1)]
        for _ in range(2 * MAX_RANGE + 1)
    ]
    # 입력을 받으면서, 최대 거리를 구해준다. => 시간초 산정
    max_x, max_y, min_x, min_y = MAX_RANGE, MAX_RANGE, MAX_RANGE, MAX_RANGE
    for i in range(n):
        x, y, w, d = tuple(input().split())
        x, y, w = map(int, [x, y, w])
        x,y = 2*x + MAX_RANGE, 2*y + MAX_RANGE
        max_x, max_y = max(max_x, x), max(max_y, y)
        min_x, min_y = min(min_x, x), min(min_y, y)
        beads.append((w, i, dir_mapper[d]))
    
    time = max(max_x, max_y) - min(min_x, min_y)
    current_conflicTime = Simulateion(time)
    ans.append(current_conflicTime)


for elem in ans:
    print(elem)