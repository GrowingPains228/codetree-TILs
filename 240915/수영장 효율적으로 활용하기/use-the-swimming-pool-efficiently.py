MaxTime = 1440

n, m = map(int, input().split())
Times = list(map(int, input().split()))
lineList = [0] * m


def is_possible(mid):
    idx = 0
    for i in range(m):
        while idx < n and lineList[i] + Times[idx] <= mid:
            lineList[i] += Times[idx]
            idx += 1

    return idx == n


left, right = 1, 10**9
ans = 10**9
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        ans = min(ans, mid)
        right = mid - 1
    else:
        left = mid + 1

    for i in range(m):
        lineList[i] = 0

print(ans)