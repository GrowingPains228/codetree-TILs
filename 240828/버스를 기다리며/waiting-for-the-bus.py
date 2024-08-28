n, m, c = tuple(map(int, input().split()))
timeLine = list(map(int, input().split()))
timeLine.sort()


def Is_Possible(time):
    global c
    idx = 0
    # 버스마다 기다리는 시간은 = time
    for i in range(m):
        people = 0
        if idx >= n:
            continue

        firstGetOnTime = timeLine[idx]
        while people < c and timeLine[idx] - firstGetOnTime <= time:
            people += 1
            idx += 1

    return idx == n


left, right = 0, 10**9
ans = 10**9
while left <= right:
    mid = (left + right)//2
    if Is_Possible(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1
print(ans)