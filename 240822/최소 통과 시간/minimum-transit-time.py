n, m = map(int, input().split())

portal = [int(input()) for _ in range(m)]
MAX_TIME = n * portal[m-1]


def IsPossible(maxTime):
    cnt = 0
    for i in range(m):
        if maxTime < portal[i]:
            continue
        cnt += maxTime // portal[i]

    return cnt >= n


left, right = 0, MAX_TIME
min_time = MAX_TIME
while left <= right:
    mid = (left + right) // 2
    if IsPossible(mid):
        min_time = min(min_time, mid)
        right = mid - 1
    else:
        left = mid + 1

print(min_time)