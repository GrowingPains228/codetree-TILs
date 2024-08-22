n, m = map(int, input().split())
dotList = [int(input()) for _ in range(n)]
dotList.sort()

MAX_DIST = dotList[n-1] - dotList[0]


def is_possible(max_dist):
    global m, MAX_DIST
    dist = 0
    cnt = 1     # 처음에 한개 설치했다고 가정
    min_dist = MAX_DIST
    for i in range(1, n):
        d = dotList[i] - dotList[i-1]

        dist += d

        if dist >= max_dist:
            min_dist = min(min_dist, dist)
            dist = 0
            cnt += 1

    return cnt >= m


left, right = 0, MAX_DIST
max_dist = 0

while left <= right:
    mid = (left + right) // 2

    if is_possible(mid):
        max_dist = max(max_dist, mid)
        left = mid + 1
    else:
        right = mid - 1

print(max_dist)