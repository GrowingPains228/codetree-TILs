class Student:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def shouting(self):
        if not self.next or not self.prev:
            print(-1)
        else:
            print(self.prev.data, self.next.data)


children = dict()
children[1] = Student(1)
curr_cnt = 1

def connect(a,b):
    if a is not None:
        a.next = b
    if b is not None:
        b.prev = a


def pushLineToNext(a, b):
    global curr_cnt

    for i in range(1, b+1):
        curr_cnt += 1
        children[curr_cnt] = Student(curr_cnt)
        if i == 1:
            continue
        else:
            connect(children[curr_cnt-1], children[curr_cnt])

    next_a_child = children[a].next
    connect(children[a], children[curr_cnt-b+1])
    connect(children[curr_cnt], next_a_child)


def pushLineToPrev(a, b):
    global curr_cnt

    for i in range(1, b+1):
        curr_cnt += 1
        children[curr_cnt] = Student(curr_cnt)
        if i == 1:
            continue
        else:
            connect(children[curr_cnt-1], children[curr_cnt])

    prev_a_child = children[a].prev
    connect(children[curr_cnt], children[a])
    connect(prev_a_child, children[curr_cnt-b+1])


q = int(input())

for _ in range(q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        pushLineToNext(cmd[1], cmd[2])
    elif cmd[0] == 2:
        pushLineToPrev(cmd[1], cmd[2])
    else:
        children[cmd[1]].shouting()