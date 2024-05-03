n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited_x = [False]*n
visited_y = [False]*n
ans = 0
ans_list = list()


def all_sum():
    sum_all = 0
    for x, y in ans_list:
        sum_all += grid[x][y]

    return sum_all


def choose(curr_num):
    global ans
    if curr_num == n:
        ans = max(ans, all_sum())
        return

    for i in range(n):
        if visited_x[i]:
            continue

        for j in range(n):
            if visited_y[j]:
                continue

            visited_x[i] = True
            visited_y[j] = True
            ans_list.append((i, j))

            choose(curr_num+1)

            ans_list.pop()
            visited_x[i] = False
            visited_y[j] = False


choose(0)
print(ans)