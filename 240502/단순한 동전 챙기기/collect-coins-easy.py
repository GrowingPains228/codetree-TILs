import sys
n = int(input())
GOAL_COIN = 3
grid = [
    list(input())
    for _ in range(n)
]
coin_pos_arr = []
start_pos, end_pos = (0, 0), (0, 0)
# n*n을 돌면서 시작 지점, 동전 위치 등을 찾아서 세팅해준다.
for i in range(n):
    for j in range(n):
        if grid[i][j] == '.':
            continue

        if grid[i][j] == 'S':
            start_pos = (i, j)
        elif grid[i][j] == 'E':
            end_pos = (i,j)
        else :
            coin_pos_arr.append((int(grid[i][j]), i, j))
coin_pos_arr.sort(key=lambda x: x[0]) # 미리 정렬해 놓으면, 순서대로 뽑아서 사용하면 되기 때문에 조합을 쉽게 만들 수 있음.
cnt_coin = len(coin_pos_arr)
ans = sys.maxsize


# 아이디어 :
# 시작점에서 3 구간을 들렀다가 마지막 도착지점으로 가야함
# 일단 시작지점과 도착지점을 알아야함. => 어딘가에 넣어놓고
# 각 동전의 위치도 어디에 저장해 둬야한다.
# 시작 지점 -> 동전1 -> 동전2 -> 동전3 -> 도착 지점
# 이런식의 로직이 가장 짧은 거리이다.
# 동전 1,2,3 의 숫자는 점점 증가해야한다 -> 조건!
def cal_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    return abs(x1-x2) + abs(y1-y2)


def find_coin_Path(count_coin, curr_pos, curr_idx, curr_distance):
    global ans, cnt_coin

    if count_coin == GOAL_COIN+1:
        ans = min(ans, curr_distance + cal_distance(curr_pos, end_pos))
        return

    # 범위 넘어 가면 리턴
    if curr_idx == cnt_coin:
        return

    coin_num, nx, ny = coin_pos_arr[curr_idx]
    #선택 했을때,
    find_coin_Path(count_coin + 1, (nx, ny), curr_idx + 1, curr_distance + cal_distance((nx, ny), curr_pos))

    # 선택 안 했을때, 현재 위치 그대로에서 다음 코인
    find_coin_Path(count_coin, curr_pos, curr_idx + 1, curr_distance)


if len(coin_pos_arr) < 3:
    ans = -1
else :
    find_coin_Path(1, start_pos, 0, 0)

print(ans)