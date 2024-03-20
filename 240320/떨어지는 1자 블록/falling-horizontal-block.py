n, m, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def get_HightestRow(start_colume, max_colume):
    Index_row = n-1

    for c in range(start_colume, max_colume + 1):
        while True:
            if not grid[Index_row][c] :
                break

            Index_row -= 1
    
    return Index_row



def fill_Entity(x, y, length):
    for i in range(y, y + length):
        grid[x][i] = 1


def simulation():
    global m, k
    height = get_HightestRow(k-1, k + m - 2)
    fill_Entity(height, k-1, m)
    

simulation()

for row in grid:
    for elem in row :
        print(elem, end = ' ')
    print()