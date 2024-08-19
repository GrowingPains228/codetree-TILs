import sys
from collections import defaultdict
n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
length = len(arr)
# 1. 특정 구간을 잡았을 때 구간 안에도 1이상 m 이하의 숫자가 전부 적어도 하나씩 존재
# 2. 구간 밖에서도 1이상 m이하의 숫자가 전부 적어도 하나씩 존재하는 경우
#[전략]
# 1. Hashmap으로 일단 숫자들의 개수를 파악
# 2. Hashset으로 숫자들의 유일성 파악
# 3. 위 Hashmap과 HashSet을 구간, 바깥 이렇게 두개 세트로 선언해서 사용한다.
inSectionMap = defaultdict(lambda: 0)
inSectionSet = set()
outSectionMap = defaultdict(lambda: 0)
for i in range(1, length):
    outSectionMap[arr[i]] += 1
outSectionSet = set(arr[1:])
minStopCnt = len(outSectionSet) # 숫자들의 종류 개수. = 멈추는 시점

j = 0
ans = sys.maxsize


# j+1 원소를 추가 했을때,
# inSectionSet 에서는 추가되는 상황
# outSectionSet 에서는 감소하는 원소일 수 있음.
def isMovable(next_j):
    if next_j >= length:
        return False

    if inSectionMap[arr[next_j]] == 0:
        return True

    if outSectionMap[arr[next_j]] == 1:
        return False

    return True


for i in range(1, length):
    while isMovable(j+1):
        inSectionMap[arr[j+1]] += 1
        inSectionSet.add(arr[j+1])
        outSectionMap[arr[j+1]] -= 1
        if outSectionMap[arr[j+1]] == 0:
            outSectionSet.remove(arr[j+1])
        j += 1
        if len(inSectionSet) == len(outSectionSet) == minStopCnt:
            break

    if len(inSectionSet) == len(outSectionSet) == minStopCnt:
        ans = min(ans, j - i + 1)

    outSectionMap[arr[i]] += 1
    outSectionSet.add(arr[i])
    inSectionMap[arr[i]] -= 1
    if inSectionMap[arr[i]] == 0:
        inSectionSet.remove(arr[i])

print(ans)