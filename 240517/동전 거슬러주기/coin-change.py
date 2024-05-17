from collections import deque

n,m = tuple(map(int, input().split()))
coins = [0] + list(map(int, input().split()))

q = deque()
visited = [False] * (m+1)

step = [0] * (m+1)
ans = 0


def in_range(num):
    return num <= m


def can_go(num):
    return in_range(num) and not  visited[num]


def push(num, value):
    visited[num] = True
    step[num] = value
    q.append(num)


def find_min_cnt():
    global ans

    while q:
        curr_num = q.popleft()

        for i in range(1,n + 1):
            if can_go(curr_num + coins[i]):
                push(curr_num + coins[i], step[curr_num]+1)

    if visited[m]:
        ans = step[m]
    else:
        ans = -1


push(0, 0)
find_min_cnt()
print(ans)