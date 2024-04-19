#입력 및 초기화
n,m = tuple(map(int, input().split()))
grid = [
    [[] for _ in range(n) ]
    for _ in range(n)
]
order = [(0,0)]*(n**2+1)
for i in range(n):
    input_list = list(map(int, input().split()))

    for j in range(n):
        grid[i][j].append(input_list[j])
        order[input_list[j]] = (i,j)

orders = list(map(int, input().split()))


# 범위 체크
def In_Range(x,y) :
    return x >= 0 and x < n and y >= 0 and y < n

# 이동해야 하는 위치를 반환
def Get_MovePos(x,y):
    dxs, dys = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]

    max_idx = 0
    max_value = 0
    for i, (dx, dy) in enumerate(zip(dxs, dys)) :
        nx, ny = x + dx, y + dy
        if not In_Range(nx, ny) :
            continue
        
        for elem in grid[nx][ny] :
            if elem > max_value :
                max_value = elem
                max_idx = i
    
    return (x + dxs[max_idx], y + dys[max_idx]) if max_value != 0 else (-1, -1)


def Move(pos, target) :
    x,y = pos
    nx, ny = Get_MovePos(x,y)
    if nx == -1 or ny == -1:
        return

    # 타겟 위치 찾기
    target_idx = -1
    for i in range(len(grid[x][y])):
        if grid[x][y][i] == target:
            target_idx = i
            break

    # 현재 타겟이 있는 넘버의 배열에서 타겟까지 꺼낸 후
    temp_arr = grid[x][y][target_idx:]
    if target_idx != 0 :
        grid[x][y] = grid[x][y][:target_idx]
    else :
        grid[x][y] = []

    #옮겨줄 위치로 넣어준다.

    grid[nx][ny].extend(temp_arr)
    for elem in temp_arr :
        order[elem] = (nx, ny)


for elem in orders :
    Move(order[elem], elem)


for i in range(n):
    for j in range(n):
        if not grid[i][j] :
            print("None")
        else :
            for elem in reversed(grid[i][j]) :
                print(elem, end = ' ')
            print()