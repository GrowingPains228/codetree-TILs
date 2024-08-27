MAX_DIST = 10**9
n = int(input())
lineList = [tuple(map(int, input().split())) for _ in range(n)]
lineList.sort()


def Is_Possible(min_dist):
    cur_x = lineList[0][0]
    for i in range(1, n):
        (x1, x2) = lineList[i]
        if cur_x + min_dist > x2:
            return False

        cur_x = cur_x if cur_x + min_dist < x1 else cur_x + min_dist

    return True


left, right = (1, MAX_DIST)
ans = 0
while left <= right:
    mid = (left + right)//2
    if Is_Possible(mid):
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)