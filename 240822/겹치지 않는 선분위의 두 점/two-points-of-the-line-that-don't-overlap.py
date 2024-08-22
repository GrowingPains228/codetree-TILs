n, m = map(int, input().split())
lines = [tuple(map(int, input().split())) for _ in range(m)]
lines.sort()
MAX_RANGE = 10**18


def is_possible(min_dist):
    global n
    cnt = 1
    (recent_dot, _) = lines[0]
    for i in range(m):
        a, b = lines[i]
        d = b - a
        # a 위치에 점이 설치되는지 유무 확인
        if a - recent_dot >= min_dist:
            recent_dot = a
            cnt += 1

        if d >= min_dist:
            cnt += d // min_dist
            recent_dot = b - d % min_dist

    return cnt >= n


left, right = 0, MAX_RANGE
max_dist = 0
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        max_dist = max(max_dist, mid)
        left = mid + 1
    else:
        right = mid - 1

print(max_dist)