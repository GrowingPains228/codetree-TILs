n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
copy_grid = []

def InRange(x1, y1, x2, y2):
    return (x1 == x2 or y1 == y2) and (abs(x2-x1) + abs(y2-y1) < grid[x2][y2])


def Bomb(x, y) :
    for i in range(n):
        for j in range(n):
            if InRange(i,j,x,y):
                copy_grid[i][j] = 0


# 다른 문제들 해설에서 n개의 메모리만 사용하는데, 한번 해보기
def grabity() :
    for i in range(n):
        temp_idx = 0
        arr_grid = [0] * n
        for j in range(n-1, -1, -1):
            if copy_grid[j][i]:
                arr_grid[temp_idx] = copy_grid[j][i]
                temp_idx += 1
        
        for j in range(n):
            copy_grid[j][i] = arr_grid[j]


def count_optimum():
    ans = 0
    # 가로 검사
    for i in range(n):
        cnt = 1
        idx = 0
        for j in range(1, n):
            if copy_grid[i][idx] == 0 :
                idx = j
                cnt = 1
                continue

            if copy_grid[i][idx] == copy_grid[i][j]:
                cnt += 1

                if j == n-1 and cnt == 2:
                    ans += 1
            else:
                if cnt == 2:
                    ans += 1
                
                idx = j
                cnt = 1
    
    # 세로 검사
    for i in range(n):
        cnt = 1
        idx = 0
        for j in range(1,n):
            if copy_grid[idx][i] == 0 :
                idx = j
                cnt = 1
                continue

            if copy_grid[idx][i] == copy_grid[j][i]:
                cnt += 1

                if j == n-1 and cnt == 2:
                    ans += 1
            else:
                if cnt == 2:
                    ans += 1
                
                idx = j
                cnt = 1

    return ans


ans = 0
for i in range(n):
    for j in range(n):
        copy_grid = grid[::]
        Bomb(i,j)
        grabity()

        ans = max(ans, count_optimum())

print(ans)