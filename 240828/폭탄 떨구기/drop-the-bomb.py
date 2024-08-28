MAX_NUM = 10*9
n, k = tuple(map(int, input().split()))
dot_list = list()
max_dot, min_dot = -1, MAX_NUM
for _ in range(n):
    num = int(input())
    max_dot = max(max_dot, num)
    min_dot = min(min_dot, num)
    dot_list.append(num)
dot_list.sort()


def is_Possible(R):
    global n, k
    # 폭탄을 떨어 뜨릴때마다 범위 안에 있는 점들을 세준다는 개념으로
    curX = dot_list[0]
    bomb_cnt = 1
    cnt = 1
    for i in range(1, n):
        if curX + 2*R >= dot_list[i]:
            cnt += 1
        else:
            curX = dot_list[i]
            bomb_cnt += 1
            if bomb_cnt > k:
                return False
            cnt += 1

    return cnt == n and bomb_cnt <= k


max_range = max_dot - min_dot
left, right = 0, max_range
ans = max_range
while left <= right:
    mid = (left + right) // 2
    if is_Possible(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1
print(ans)