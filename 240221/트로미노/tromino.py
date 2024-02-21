n,m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

shapes = [[[1, 0, 0],
          [1, 1, 0],
          [0, 0, 0]],

          [[1, 1, 0],
          [0, 1, 0],
          [0, 0, 0]],

          [[0, 1, 0],
          [1, 1, 0],
          [0, 0, 0]],

          [[1, 1, 0],
          [1, 0, 0],
          [0, 0, 0]],

          [[1, 1, 1],
          [0, 0, 0],
          [0, 0, 0]],

          [[1, 0, 0],
          [1, 0, 0],
          [1, 0, 0]],
]

def get_max_sum(x,y) :
    max_sum = 0
    for i in range(len(shapes)) :
        if_possible = True
        sum_of_nums = 0
        for dy in range(3):
            for dx in range(3) :
                if shapes[i][dy][dx] == 0 :
                    continue
                if x + dx >= m or y + dy >= n :
                    if_possible = False
                else :
                    sum_of_nums += grid[y + dy][x + dx]
                
        if if_possible :
            max_sum = max(max_sum, sum_of_nums)

    return max_sum

ans = 0
for i in range(n) :
    for j in range(m) :
        ans = max(ans, get_max_sum(j,i))

print(ans)