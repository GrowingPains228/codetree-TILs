from collections import deque
MAX_RANGE = 1000000
# 입력
n = int(input())

# BFS를 위한
visited = [False] * (MAX_RANGE + 1)
step = [0] * (MAX_RANGE + 1)
queue = deque()


def calculate_type(type, value):
    if type == 0:
        return value // 3
    elif type == 1:
        return value // 2
    elif type == 2:
        return value + 1
    else :
        return value - 1


def push(idx, s):
    visited[idx] = True
    step[idx] = s
    queue.append(idx)


def can_go(idx):
    return 0 <= idx < MAX_RANGE + 1 and not visited[idx]


def bfs():
    dxs = [0, 1, 2, 3]

    while queue:
        idx = queue.popleft()
        for dx in dxs:
            if (dx == 0 and idx % 3 > 0) or (dx == 1 and idx % 2 > 0):
                continue

            new_idx = calculate_type(dx, idx)

            if can_go(new_idx):
                push(new_idx, step[idx] + 1)


push(n, 0)
bfs()
print(step[1])