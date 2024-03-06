n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
r,c = tuple(map(int, input().split()))
end_of_temp = n


def Bomb(r,c):
    power = grid[r][c] -1

    # 세로부분 터트리기
    st_idx = (r - power) if (r - power) >= 0 else 0
    end_idx = (r + power) if (r + power) < n else n-1
    for i in range(st_idx, end_idx+1):
        grid[i][c] = 0
    
    # 가로 부분 터트리기
    st_idx = (c - power) if (c - power) >= 0 else 0
    end_idx = (c + power) if (c + power) < n else n-1
    for i in range(st_idx, end_idx+1):
        grid[r][i] = 0


# temp를 만들어서 복사하는 방법
def Apply_Gravity():
    global grid
    temp = [[0]*n for _ in range(n)]
    for i in range(n):
        end_of_temp = n-1
        for j in range(n-1, -1, -1):
            if grid[j][i] == 0:
                continue
            temp[end_of_temp][i] = grid[j][i]
            end_of_temp -= 1
    
    grid = [
        temp[i] for i in range(n)
    ]


Bomb(r-1,c-1)
Apply_Gravity()

for row in grid :
    for elem in row:
        print(elem, end= ' ')
    print()