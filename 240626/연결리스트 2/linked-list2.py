class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


nodes = dict()
num = int(input())
for i in range(1, num+1):
    nodes[i] = Node(i)

q = int(input())
command_list = [
    input() for _ in range(q)
]

for command in command_list:
    cl = tuple(map(int, command.split()))
    if cl[0] == 1 :
        new_node = nodes[cl[1]]
        if new_node.next is not None:
            new_node.next.prev = new_node.prev
        if new_node.prev is not None:
            new_node.prev.next = new_node.next

        new_node.prev = None
        new_node.next = None
    elif cl[0] == 2 :
        singleton_node = nodes[cl[2]]   # j번 노드
        inserted_node = nodes[cl[1]]     # i번 노드

        singleton_node.next = inserted_node
        singleton_node.prev = inserted_node.prev

        if singleton_node.prev is not None:
            singleton_node.prev.next = singleton_node
        if singleton_node.next is not None:
            singleton_node.next.prev = singleton_node
    elif cl[0] == 3:
        singleton_node = nodes[cl[2]]   # j번 노드
        inserted_node = nodes[cl[1]]     # i번 노드

        singleton_node.prev = inserted_node
        singleton_node.next = inserted_node.next

        if singleton_node.next is not None:
            singleton_node.next.prev = singleton_node
        if singleton_node.prev is not None:
            singleton_node.prev.next = singleton_node
    else:
        print(nodes[cl[1]].prev.data if nodes[cl[1]].prev else 0, end = " ")
        print(nodes[cl[1]].next.data if nodes[cl[1]].next else 0)

for i in range(1, num+1):
    if nodes[i].next :
        print(nodes[i].next.data, end = " ")
    else:
        print(0, end = " ")