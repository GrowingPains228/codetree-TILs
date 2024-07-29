from sortedcontainers import SortedDict

n, q = tuple(map(int, input().split()))
dotList = list(map(int, input().split()))
dotToIndex = dict()
sm = SortedDict()
for key in dotList:
    sm[key] = True

qList = list()

# 단순히 질의에 대한 범위는 False로.
for _ in range(q):
    a, b = tuple(map(int, input().split()))
    qList.append((a, b))
    sm[a] = False if a not in sm else True
    sm[b] = False if b not in sm else True

for index, key in enumerate(sm.keys(), start=1):
    dotToIndex[key] = index

sumList = list(0 for _ in range(len(sm)+1))   # index 순으로 Sum 한 리스트!
for index, key in enumerate(dotToIndex.keys(), start=1):
    sumList[index] = sumList[index-1] + 1 if sm[key] else sumList[index-1]


for (x, y) in qList:
    print(sumList[dotToIndex[y]] - sumList[dotToIndex[x]-1])