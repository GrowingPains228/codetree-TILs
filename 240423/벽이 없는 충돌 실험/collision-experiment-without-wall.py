MAX_RANGE = 1000
TEST_CASE = int(input())
grid = [ [-1]* (4*MAX_RANGE) for _ in range(4*MAX_RANGE) ]
next_grid = [ [-1]* (4*MAX_RANGE) for _ in range(4*MAX_RANGE)]
ans = []
beads = []

def In_Range(x,y):
    return 0 <= x and x < 4*MAX_RANGE and 0 <= y and y < 4*MAX_RANGE


# 튕기는 경우도 없고, 떨어지는 경우도 고려 안해도됨.
# 계속 굴러 간다는 의미!
def Get_NextPos(x, y, idx):
    dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
    (w, d) = beads[idx]
    nx, ny = x + dxs[d], y + dys[d]

    return (nx, ny)


def Move_all():
    IsConflict = False
    for y in range(4*MAX_RANGE):
        for x in range(4*MAX_RANGE):
            if grid[y][x] == -1 :
                continue

            idx = grid[y][x]
            next_x, next_y = Get_NextPos(x, y, idx)
            next_idx = next_grid[next_y][next_x]

            if next_idx == -1:
                next_grid[next_y][next_x] = idx
            else:
                IsConflict = True
                (w1, _), (w2, _) = beads[next_idx], beads[idx]
                if w1 > w2 :
                    continue
                elif w1 < w2 :
                    next_grid[next_y][next_x] = idx
                else :
                    next_grid[next_y][next_x] = max(next_idx, idx)

    return IsConflict

def Simulateion(time):
    t = -1

    for i in range(1, time+1):
        IsConflict = False
        # 초기화
        for y in range(4*MAX_RANGE) :
            for x in range(4*MAX_RANGE):
                next_grid[y][x] = -1
        
        # 이동 및 충돌 체크
        IsConflict = Move_all()

        # 복사
        for y in range(4*MAX_RANGE) :
            for x in range(4*MAX_RANGE):
                grid[y][x] = next_grid[y][x]
        
        # 충돌 시간 체크
        if IsConflict :
            t = i

    return t


dir_mapper = {
    'U' : 0,
    'R' : 1,
    'L' : 2,
    'D' : 3
}


for _ in range(TEST_CASE):
    n = int(input())
    beads = [(-1, -1) for _ in range(n)]
    for y in range(4*MAX_RANGE) :
        for x in range(4*MAX_RANGE):
            grid[y][x] = -1
    # 입력을 받으면서, 최대 거리를 구해준다. => 시간초 산정
    max_x, max_y, min_x, min_y = -1, -1, 4*MAX_RANGE, 4*MAX_RANGE
    for i in range(n):
        x, y, w, d = tuple(input().split())
        x, y, w = map(int, [x, y, w])
        x,y = 2*(x + MAX_RANGE), 2*(y + MAX_RANGE)
        max_x, max_y = max(max_x, x), max(max_y, y)
        min_x, min_y = min(min_x, x), min(min_y, y)
        beads[i] = (w, dir_mapper[d])
        grid[y][x] = i # 인덱스 값 표시
    
    time = max(max_x, max_y) - min(min_x, min_y)
    current_conflicTime = Simulateion(time)
    ans.append(current_conflicTime)


for elem in ans:
    print(elem)