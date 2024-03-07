n = 4
#입력받기
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
direction = input()


# 입력받은 방향으로 미는 함수
def dir_Push(direction):
    # 시작점 초기화 [R, L, U, D]
    # [U,L], [D, R] 이랑 시작 위치 같음,
    if direction in ['R', 'D']:
        for i in range(n-1, -1, -1):
            st = n-1
            for j in range(n-2, -1, -1):
                if direction == 'R':
                    if grid[i][j] == 0:
                        continue

                    if grid[i][st] == grid[i][j]:
                        grid[i][st] += grid[i][j]
                        grid[i][j] = 0
                    
                    st = j
                else :
                    if grid[j][i] == 0:
                        continue

                    if grid[st][i] == grid[j][i]:
                        grid[st][i] += grid[j][i]
                        grid[j][i] = 0
                    
                    st = j
    else : # L, U 경우
        for i in range(n):
            st = 0
            for j in range(1, n):
                if direction == 'L':

                    if grid[i][j] == 0:
                        continue

                    if grid[i][st] == grid[i][j]:
                        grid[i][st] += grid[i][j]
                        grid[i][j] = 0
                    
                    st = j
                else :
                    if grid[i][j] == 0:
                        continue

                    if grid[st][i] == grid[j][i]:
                        grid[st][i] += grid[j][i]
                        grid[j][i] = 0
                    
                    st = j
        

def Combine_grid(direction):
    temp = [[0]*4 for _ in range(n)]

    if direction in ['L', 'U']:
        for i in range(n):
            temp_idx = 0
            for j in range(n):
                if direction == 'L':
                    if grid[i][j] != 0:
                        temp[i][temp_idx] = grid[i][j]
                        temp_idx += 1
                else : # U
                    if grid[j][i] != 0:
                        temp[temp_idx][i] = grid[j][i]
                        temp_idx += 1                    
    else :
        for i in range(n-1, -1, -1):
            temp_idx = n-1
            for j in range(n-1, -1, -1):
                if direction == 'R':
                    if grid[i][j] != 0:
                        temp[i][temp_idx] = grid[i][j]
                        temp_idx -= 1
                else: # D
                    if grid[j][i] != 0:
                        temp[temp_idx][i] = grid[j][i]
                        temp_idx -= 1

    for r,row in enumerate(temp):
        for c,elem in enumerate(row):
            grid[r][c] = elem

dir_Push(direction)
Combine_grid(direction)
for row in grid:
    for elem in row:
        print(elem, end = " ")
    print()