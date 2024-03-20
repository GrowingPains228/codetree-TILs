n, m, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

#해당 row의 [col_s, col_e] 열에
#전부 블럭이 없는지를 확인
def all_blank(row, col_s, col_e):
    return all([
        not grid[row][col]
        for col in range(col_s, col_e+1)
    ])


def get_target_row():
    for row in range(n-1):
        if not all_blank(row + 1, k, k + m - 1):
            return row
    
    return n - 1

k -= 1

#최종적으로 멈추게 될 위치를 구한다.
target_row = get_target_row()

for col in range(k, k+m):
    grid[target_row][col] = 1

for row in grid:
    for elem in row:
        print(elem, end = ' ')
    print()