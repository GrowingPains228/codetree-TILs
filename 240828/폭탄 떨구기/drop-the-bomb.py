MAX_NUM = 10**9
n, k = tuple(map(int, input().split()))
dot_list = [int(input()) for _ in range(n)]
dot_list.sort()


def is_Possible(R):
    global n, k
    # 폭탄을 떨어 뜨릴때마다 범위 안에 있는 점들을 세준다는 개념으로
    cnt = 1
    idx = 0
    for i in range(n):
        if dot_list[i] - dot_list[idx] <= 2*R:
            continue
        else:
            cnt += 1
            idx = i
    return cnt <= k


left, right = 0, MAX_NUM
ans = MAX_NUM
while left <= right:
    mid = (left + right) // 2
    if is_Possible(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1
print(ans)