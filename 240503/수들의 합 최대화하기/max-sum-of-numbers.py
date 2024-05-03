n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited_x = [False]*n
visited_y = [False]*n
ans = 0


def choose(curr_num, sum_cnt):
    global ans
    if curr_num == n:
        ans = max(ans, sum_cnt)
        return

    visited_x[curr_num] = True

    for j in range(n):
        if visited_y[j]:
            continue

        visited_y[j] = True
        sum_cnt += grid[curr_num][j]

        choose(curr_num+1, sum_cnt)

        visited_y[j] = False
        sum_cnt -= grid[curr_num][j]

    visited_x[curr_num] = False


choose(0, 0)
print(ans)