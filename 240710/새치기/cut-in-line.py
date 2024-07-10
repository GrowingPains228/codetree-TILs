class Node:
    def __init__(self, data, lineNum):
        self.data = data
        self.lineNum = lineNum
        self.prev = None
        self.next = None


def connect(a,b):
    if a is not None:
        a.next = b
    if b is not None:
        b.prev = a


class Line:
    def __init__(self, i):
        self.cnt = 0
        self.head = Node(-1,i)

    def printLine(self):
        if self.cnt == 0:
            print(-1)
            return

        nextPerson = self.head.next
        while nextPerson is not None:
            print(nextPerson.data, end = " ")
            nextPerson = nextPerson.next

    def AddPeople(self, enumeration):
        connect(self.head, enumeration[0])
        self.cnt += len(enumeration)


# 입력
n, m, q = map(int, input().split())

# 사람 만큼 초기화
peopleDic = dict()

lines = [None] * m
for i in range(m):
    inputList = list(map(int, input().split()))
    peopleArray = inputList[1::]
    for num in peopleArray:
        peopleDic[num] = Node(num, i)

    peopleList = [peopleDic[elem] for elem in peopleArray]

    # 각 사람들 연결시켜주기
    for j in range(1, inputList[0]):
        connect(peopleList[j-1], peopleList[j])

    lines[i] = Line(i)
    lines[i].AddPeople(peopleList)

# b사람 앞에 a가 새치기 하는 함수
def CutInLine(a, b):
    #a가 있던 라인의 앞 사람과 뒷 사람을 이어준다.
    connect(a.prev, a.next)

    # a가 있던 라인 업데이트
    lines[a.lineNum].cnt -= 1

    # b의 이전 사람과 a를 이어준다
    connect(b.prev, a)
    # a와  b를 이어준다.
    connect(a, b)

    # b가 있던 라인 업데이트 해주기
    a.lineNum = b.lineNum
    lines[b.lineNum].cnt += 1


def CutInLines(a, b, c):
    countPeople = 0
    countNode = a
    while countNode == b:
        countPeople += 1
        countNode = countNode.next
    countPeople += 1

    #a가 있던 라인의 앞 사람과 뒷 사람을 이어준다.
    connect(a.prev, b.next)
    # a가 있던 라인 업데이트
    lines[a.lineNum].cnt -= countPeople

    # c의 이전 사람과 a를 잇는다
    connect(c.prev, a)
    # a와  c를 잇는다
    connect(b, c)

    countNode = a
    idx = c.lineNum
    while countNode == b:
        countNode.lineNum = idx
    b.lineNum = idx
    lines[idx].cnt += countPeople


def GoHome(a):
    lines[a.lineNum].cnt -= 1

    #a가 있던 라인의 앞 사람과 뒷 사람을 이어준다.
    connect(a.prev, a.next)
    #a 지운다.
    a.prev = a.next = None


for _ in range(q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        CutInLine(peopleDic[cmd[1]], peopleDic[cmd[2]])
    elif cmd[0] == 2:
        GoHome(peopleDic[cmd[1]])
    else:
        CutInLines(peopleDic[cmd[1]], peopleDic[cmd[2]], peopleDic[cmd[3]])

for line in lines:
    line.printLine()
    print()