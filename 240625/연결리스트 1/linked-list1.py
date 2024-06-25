class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


start_string = input()
cur = Node(start_string)
num = int(input())

for _ in range(num):
    commands = input().split()
    if commands[0] == '3':
        if cur.prev is not None:
            cur = cur.prev
    elif commands[0] == '4':
        if cur.next is not None:
            cur = cur.next
    elif commands[0] == '1':
        new_node = Node(commands[1])
        new_node.next = cur
        new_node.prev = cur.prev

        if new_node.next is not None:
            new_node.next.prev = new_node
        if new_node.prev is not None:
            new_node.prev.next = new_node
    else:
        new_node = Node(commands[1])
        new_node.prev = cur
        new_node.next = cur.next

        if new_node.prev is not None:
            new_node.prev.next = new_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    
    print(cur.prev.data if cur.prev else "(Null)", end = " ")
    print(cur.data, end = " ")
    print(cur.next.data if cur.next else "(Null)")