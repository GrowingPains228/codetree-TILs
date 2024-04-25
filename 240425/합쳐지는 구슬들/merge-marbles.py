import copy

# 입력
n, m, t = tuple(map(int, input().split()))
max_weight = 0
# 판 생성
grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]
# 다음 임시 판 생성
next_grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]

dir_mapper = {
    'U' : 0,
    'R' : 1,
    'L' : 2,
    'D' : 3
}

for i in range(1,m +1):
    r, c, dirr, w = tuple(input().split())
    r, c, w = map(int, [r, c, w])
    max_weight = max(max_weight, w)
    grid[r-1][c-1].append((i, w, dir_mapper[dirr]))

# 범위 체크 함수
def In_Range(x,y):
    return 0 <= x < n and 0 <= y < n


# 다음 위치와 방향 반환
# 벽에 있다면, 방향만 반대로 해서 돌려준다. ( 방향 바꾸는데 1초 소요)
def Get_Next_Pos(x, y, dirr):
    dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
    nx, ny = x + dxs[dirr], y + dys[dirr]
    if not In_Range(nx, ny):
        dirr = 3 - dirr
        return (x, y, dirr)
    
    return (nx, ny, dirr)


# 이동 함수
def move(x,y, marble):
    (num, weight, dirr) = marble
    next_x, next_y, next_dir = Get_Next_Pos(x,y, dirr)
    next_grid[next_x][next_y].append((num, weight, next_dir))


# 모든 요소 이동 함수
def All_move():
    for i in range(n):
        for j in range(n):
            for marble in grid[i][j]:
                move(i, j, marble)
    

# 충돌 체크
def IsCrash(x,y):
    return len(next_grid[x][y]) >= 2


# 충돌 했을때 합치는 함수
def Combine(marble1, marble2):
    global max_weight
    (num1, weight1, dirr1) = marble1
    (num2, weight2, dirr2) = marble2
    sum_weight = weight1 + weight2
    new_marble = (num1, sum_weight, dirr1) if num1 > num2 else (num2, sum_weight, dirr2)

    # 가장 무거운 구슬의 무게 업데이트
    max_weight = max(max_weight, sum_weight)
    return new_marble


# 모든 충돌여부 체크 및 합치기 처리
def Coordinate():
    for r in range(n):
        for c in range(n):
            # 충돌을 했다면,
            # 일단 하나 꺼낸 후, 비교해 가면서 합쳐준다.
            if IsCrash(r,c):
                new_marble = next_grid[r][c].pop()
                
                while len(next_grid[r][c]) > 0 :
                    new_marble = Combine(new_marble, next_grid[r][c].pop())
                
                next_grid[r][c].append(new_marble)


def simulate():
    global grid, next_grid
    # 초기화
    next_grid = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]
    # 모두 움직여 주고
    All_move()

    # 충돌 된 후 체크
    Coordinate()

    # 복사
    grid = copy.deepcopy(next_grid)


for _ in range(t) :
    simulate()

sum_ans = 0
for i in range(n):
    for j in range(n):
        sum_ans += len(grid[i][j])

print(sum_ans, max_weight)