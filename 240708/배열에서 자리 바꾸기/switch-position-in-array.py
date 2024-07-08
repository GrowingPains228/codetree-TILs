class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def connect(s, e):
    if s is not None:
        s.next = e
    if e is not None:
        e.prev = s
    

def pop_range_and_insert_prev(s, e, v):
    connect(s.prev, e.next)
    
    s.prev = e.next = None

    connect(v.prev, s)
    connect(e, v)
    

n = int(input())
array_node = [Node(i) for i in range(0, n+2)]
dll = array_node[0]
head = array_node[0]
tail = array_node[n+1]
# Node 1 에서 마지막 까지 연결해주기.
for i in range(1, n+2):
    connect(dll, array_node[i])
    dll = dll.next

q = int(input())

for _ in range(q):
    cmd = list(map(int, input().split()))
    node1, node2, node3, node4 = array_node[cmd[0]], array_node[cmd[1]], array_node[cmd[2]], array_node[cmd[3]]
    next_node = node2.next
    if next_node.data == node3.data:
        pop_range_and_insert_prev(node3, node4, node1)
        continue

    pop_range_and_insert_prev(node1, node2, node3)
    pop_range_and_insert_prev(node3, node4, next_node)


node = head.next
while node != tail:
    print(node.data, end = " ")
    node = node.next