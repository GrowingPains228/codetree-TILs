from sortedcontainers import SortedSet

n, q = tuple(map(int, input().split()))
dotList = list()

for _ in range(n):
    x, y = tuple(map(int, input().split()))
    dotList.append((x, y))

dotList.sort(key=lambda x: (x[0], x[1]))
dotSet = SortedSet(dotList)

for _ in range(q):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    ans = 0
    startIdx = dotSet.bisect_left((x1, _)) # 첫번째 x 점 위치 찾고
    endIdx = dotSet.bisect_right((x2, _)) # 두번째 x 점 위치 찾기

    if endIdx <= len(dotSet)-1 and x2 == dotSet[endIdx][0]:
        endIdx += 1

    for i in range(startIdx, endIdx):
        (_, y) = dotList[i]
        if y1 <= y <= y2:
            ans += 1

    print(ans)