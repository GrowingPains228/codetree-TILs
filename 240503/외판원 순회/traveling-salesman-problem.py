import sys

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [False] * n
path_arr = []
ans = sys.maxsize


def move_go(curr_num, curr_idx, path_cnt):
    global ans
    if curr_num == n-1:
        ans = min(ans, path_cnt + grid[curr_idx][0])
        return

    for i in range(1, n):
        if visited[i] or grid[curr_idx][i] == 0:
            continue

        visited[i] = True
        move_go(curr_num + 1, i, path_cnt + grid[curr_idx][i])
        visited[i] = False


visited[0] = True
move_go(0,0,0)
print(ans)