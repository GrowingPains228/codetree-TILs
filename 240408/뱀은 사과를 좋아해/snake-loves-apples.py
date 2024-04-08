import sys
# 사과 = 2
# 뱀 = 1
n, m, k = tuple(map(int, input().split()))
apple_pos = [
    tuple(map(int, input().split()))
    for _ in range(m)
]
direction_arr = [
    tuple(input().split())
    for _ in range(k)
]

dx_arr, dy_arr = [0, 0, -1, 1], [1, -1, 0, 0]
dirt_dict = {
    'R' : 0,
    'L' : 1,
    'U' : 2,
    'D' : 3
}

grid = [[0]*n for _ in range(n)]
snake = [(0,0)] # 현재 헤드만 있음.
time = 0

# 사과 위치에 사과 추가하기
for (x,y) in apple_pos :
    grid[x-1][y-1] = 2


def In_Range(x,y) :
    return x >= 0 and x < n and y >= 0 and y < n


def GameOver(t):
    print(t)
    sys.exit()


def Move(d) :
    global time
    time += 1
    x,y = snake[0] # 뱀 머리
    index = dirt_dict[d]
    dx, dy = x + dx_arr[index], y + dy_arr[index] #다음 이동할 위치
    # 게임 끝날 조건 입력
    if not In_Range(dx, dy) :
        GameOver(time)
    
    # 사과 있으면, 뱀 꼬리 한개 늘여주고
    if grid[dx][dy]:
        snake.append(snake[len(snake)-1])
        # 뱀 옮겨주기
        for i in range(len(snake)-2, 0, -1):
            snake[i] = snake[i-1]

        grid[dx][dy] = 0
    else :
        for i in range(len(snake)-1, 0, -1):
            snake[i] = snake[i-1]

    snake[0] = (dx,dy)

    if (dx, dy) in snake[1:] :
        GameOver(time)

for (d, length) in direction_arr :
    for _ in range(int(length)) :
        Move(d)

print(time)