MAX_SIZE = 10001
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [False]*n
ans = 0


def chooose(curr_num, curr_idx, value):
    global ans
    if curr_num == n:
        ans = max(ans, value)
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        chooose(curr_num+1, curr_idx+1, min(value, grid[curr_idx][i]))
        visited[i] = False


chooose(0, 0, MAX_SIZE)
print(ans)