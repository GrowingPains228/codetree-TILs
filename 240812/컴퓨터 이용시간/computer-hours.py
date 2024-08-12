from sortedcontainers import SortedSet

class Person:
    def __init__(self, index):
        self.Id = index

    def setUsingComputer(self, usingCom):
        self.usingCom = usingCom

    def getUsingComputer(self):
        return self.usingCom


n = int(input())
people = [Person(i) for i in range(0, n+1)]
useList = [tuple(map(int, input().split())) for _ in range(n)]
segments = list()
for index, (p, q) in enumerate(useList, start=1):
    segments.append((p, 1, index))
    segments.append((q, -1, index))

# PC 리스트 초기화
pcList = SortedSet()
for i in range(1, n+1):
    pcList.add(i)

segments.sort()
segs = set()

for time, v, index in segments:
    if v == 1:
        # 컴퓨터 사용
        people[index].setUsingComputer(pcList.pop(0))
        segs.add(index)
    else:
        segs.remove(index)
        # 사용하던 컴퓨터 반환
        pcList.add(people[index].getUsingComputer())

for i in range(1, n+1):
    print(people[i].getUsingComputer(), end=' ')