n,m,k = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
temp = [ [0]*n for _ in range(n)]
isChanged = False


def Bomb():
    global isChanged
    isChanged = False
    for i in range(n) :
        target_index = n-1
        cnt = 0
        for j in range(n-1, -1, -1):  
            if grid[target_index][i] == grid[j][i]:
                cnt += 1

                if j == 0 and cnt >= m:
                    for k in range(target_index, target_index - cnt, -1):
                        grid[k][i] = 0
                        isChanged = True
            else : 
                if cnt >= m:
                    for k in range(target_index, target_index - cnt, -1):
                        grid[k][i] = 0
                        isChanged = True

                target_index = j
                cnt = 1

    Apply_Grabity()

# 90도 돌려주기
def Rotate():
    temp = [
        [grid[n-1-i][j] for i in range(n)]
        for j in range(n)
    ]

    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]

    Apply_Grabity()



# 중력 작용
def Apply_Grabity():
    temp = [ [0]*n for _ in range(n) ]

    for i in range(n):
        index = n-1
        for j in range(n-1,-1, -1):
            if grid[j][i] == 0:
                continue
            
            temp[index][i] = grid[j][i]
            index -= 1

    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]


# 디버그를 위한 프린트 함수
def Print_Grid(log):
    print(log)
    for row in grid:
        for elem in row:
            print(elem, end = " ")
        print()


for _ in range(k):
    Bomb()
    Rotate()

# 일단 터트려 보고, 
while True:
    Bomb()
    #터트리기 전 상태와 터트린 후의 상태가 같다면 Stop
    if isChanged:
        break

ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] > 0 :
            ans += 1

print(ans)