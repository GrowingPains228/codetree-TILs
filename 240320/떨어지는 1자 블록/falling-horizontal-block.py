n, m, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 밑에서 부터 1이 채워져 있다고 가정하고 짠 함수 (* 근데, 테스트 케이스는 그게 아니었음)
def get_HightestRow(start_colume, max_colume):
    Index_row = n-1

    for c in range(start_colume, max_colume + 1):
        while True:
            if not grid[Index_row][c] :
                break

            Index_row -= 1
    
    return Index_row

# 범위 안에서 전부 탐색하며 제일 위쪽 열의 Index를 반환하는 함수
def get_HightestRow2(start_colume, max_colume):
    Index_row = n-1

    for c in range(start_colume, max_colume + 1):
        for r in range(n-1, 0, -1):
            if grid[r][c] :
                Index_row = min(Index_row, r)
    
    return Index_row if Index_row == n-1 else Index_row -1


def fill_Entity(x, y, length):
    for i in range(y, y + length):
        grid[x][i] = 1


def simulation():
    global m, k
    height = get_HightestRow2(k-1, k + m - 2)
    fill_Entity(height, k-1, m)
    

simulation()

for row in grid:
    for elem in row :
        print(elem, end = ' ')
    print()