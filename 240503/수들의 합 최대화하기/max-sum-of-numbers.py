n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited_x = [False]*n
visited_y = [False]*n
ans = 0
ans_list = list()


def Is_not_line():
    x1, y1 = ans_list[0]
    x2, y2 = ans_list[1]
    x3, y3 = ans_list[2]
    return x1 != x2 != x3 and y1 != y2 != y3


def all_sum():
    sum_all = 0
    for x, y in ans_list:
        sum_all += grid[x][y]

    return sum_all


def choose(curr_num):
    global ans
    if curr_num == n:
        if Is_not_line():
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