def connect(a,b):
    if a is not None:
        a.next = b
    if b is not None:
        b.prev = a


class Person:
    def __init__(self, name):
        self.name = name
        self.lineNum = -1
        self.prev = None
        self.next = None


class Line:
    def __init__(self):
        self.head = Person("")
        self.tail = self.head
        self.cnt = 0

    def LinkPerson(self, person):
        connect(self.tail, person)
        self.tail = person
        self.cnt += 1

    def printAll(self):
        if self.cnt == 0:
            print(-1)
            return

        curPerson = self.head.next
        while curPerson is not None:
            print(curPerson.name, end = " ")
            curPerson = curPerson.next
        print()



n, m, q = map(int, input().split())

# 라인 초기화
lineGroup = [None] * m
for i in range(m):
    lineGroup[i] = Line()

peopleDic = dict()
inputName = [""] + list(input().split())

x = n//m
for i in range(1, n+1):
    newPerson = Person(inputName[i])
    lineIdx = (i-1) // x
    newPerson.lineNum = lineIdx
    peopleDic[inputName[i]] = newPerson
    lineGroup[lineIdx].LinkPerson(newPerson)

def CutInFront(a,b):
    connect(a.prev, a.next)
    lineGroup[a.lineNum].cnt -= 1

    connect(b.prev, a)
    connect(a, b)
    lineGroup[b.lineNum].cnt += 1


def CutInFrontGroup(a, b, c):
    lenPeople = 0
    node = a
    while node is not None:
        lenPeople += 1
        node = node.next
        if node == b:
            lenPeople += 1
            break

    connect(a.prev, b.next)
    lineGroup[a.lineNum].cnt -= lenPeople

    connect(c.prev, a)
    connect(b, c)
    lineGroup[c.lineNum].cnt += lenPeople


def GoHome(a):
    connect(a.prev, a.next)
    a.prev = a.next = None
    lineGroup[a.lineNum].cnt -= 1
    a.lineNum = -1


for _ in range(q):
    cmd = input().split()

    if cmd[0] == "1":
        person1, person2 = peopleDic[cmd[1]], peopleDic[cmd[2]]
        CutInFront(person1, person2)
    elif cmd[0] == "2":
        person = peopleDic[cmd[1]]
        GoHome(person)
    else:
        person1, person2, person3 = peopleDic[cmd[1]], peopleDic[cmd[2]], peopleDic[cmd[3]]
        CutInFrontGroup(person1, person2, person3)


for line in lineGroup:
    line.printAll()