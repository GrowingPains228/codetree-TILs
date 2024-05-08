import collections
SELECT_ROCK = True
RESET_ROCK = False


# 입력 받기
n, k, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [ [False] * n for _ in range(n) ]
# 큐 생성
bfs_queue = collections.deque()
start_pos_Group = list()
# 시작 점들 입력 받기
for _ in range(k):
    x, y = tuple(map(int, input().split()))
    x, y = x - 1, y - 1
    start_pos_Group.append((x, y))


# 돌만 따로 담아두고 그것들을 백트래킹으로 모든 경우의 수를 뽑아주자.
Rock_Group = list()
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            Rock_Group.append((i,j))
MAX_ROCK_INDEX = len(Rock_Group)
tf_rockGroup = [False] * MAX_ROCK_INDEX

ans = 0


# 돌을 치우는 모든 경우를 구하려면
# 조합을 이용하는 것이 가장 간단해 보인다.
# 앞에서 배운 백 트래킹으로 구현해보자.
def Select_rocks(curr_num, curr_cnt):
    global ans

    if curr_num == MAX_ROCK_INDEX :
        if curr_cnt == m:
            # 여기에 격자 칸을 세어주는 로직을 넣어준다!
            Initialize()
            Erase_Rock(True)
            ans = max(ans, bfs())
            Erase_Rock(False)
        return

    tf_rockGroup[curr_num] = True
    Select_rocks(curr_num + 1, curr_cnt + 1)

    tf_rockGroup[curr_num] = False
    Select_rocks(curr_num + 1, curr_cnt)


def In_Range(x, y):
    return 0 <= x < n and 0 <= y < n


def Initialize():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    for z in range(k):
        bfs_queue.append(start_pos_Group[z])
        visited[x][y] = True


# 돌은 제외할때 = True, 돌을 리셋할때 = False
def Erase_Rock(tf):
    for i in range(MAX_ROCK_INDEX):
        if tf_rockGroup[i]:
            x, y = Rock_Group[i]

            if tf:
                grid[x][y] = 0
            else:
                grid[x][y] = 1


def can_go(x,y):
    return In_Range(x,y) and not visited[x][y] and grid[x][y] == 0


def bfs():
    cnt = 1
    dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]
    while bfs_queue:
        x,y = bfs_queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                cnt += 1
                bfs_queue.append((nx, ny))

    return cnt


Select_rocks(0, 0)
print(ans)