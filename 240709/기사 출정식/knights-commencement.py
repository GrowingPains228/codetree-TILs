class Knight:
    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None

    def Shouting(self):
        if self.prev is None or self.next is None:
            return

        print(self.prev.id, self.next.id)


def connect(a,b):
    if a is not None:
        a.next = b
    if b is not None:
        b.prev = a


n, m = map(int, input().split())
inputGroup = list(map(int, input().split()))
knightDict = dict()

for elem in inputGroup:
    knightDict[elem] = Knight(elem)

for i in range(1, n):
    connect(knightDict[inputGroup[i]], knightDict[inputGroup[i-1]])
connect(knightDict[inputGroup[0]], knightDict[inputGroup[n-1]])


def callOutOne(id):
    knight = knightDict[id]
    knight.Shouting()

    connect(knight.prev, knight.next)
    knight.next = knight.prev = None


for _ in range(m):
    num = int(input())
    callOutOne(num)