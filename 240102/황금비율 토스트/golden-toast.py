# 노드 클래스를 만들어줌
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
        self.prev = None

# 이중 연결 리스트 클래스를 만들어줌.
class DoublyLinkedList :
    def __init__(self) :
        self.END = Node(-1) #구현의 편의를 위해 dummy 값을 넣어놓고 시작
        self.head = self.END
        self.tail = self.END
    
    def push_front(self, new_data) :
        new_node = Node(new_data)
        new_node.next = self.head

        self.head.prev = new_node
        self.head = new_node
        new_node.prev = None
    
    def push_back(self, new_data) :
        if self.begin() == self.end() :
            self.push_front(new_data)
        else :
            new_node = Node(new_data)
            new_node.prev = self.tail.prev
            self.tail.prev.next = new_node
            new_node.next = self.tail
            self.tail.prev = new_node
    
    def erase(self, node) :
        next_node = node.next

        if node == self.begin() : 
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
        else : 
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None
        
        return next_node

    def insert(self, node, new_data) :
        if node == self.end() :
            self.push_back(new_data)

        elif node == self.begin() :
            self.push_front(new_data)

        else :
            new_node = Node(new_data)
            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node
    
    def begin(self) :
        return self.head
    
    def end(self) :
        return self.tail

n, m = tuple(map(int, input().split()))
string = input()
breads = DoublyLinkedList()

for i in range(n) :
    breads.push_back(string[i])

it = breads.end()

for _ in range(m) :
    command = input().split()
    
    if command[0] == 'L' :
        if it == breads.begin() :
            continue
        
        it = it.prev
    elif command[0] == 'R' :
        if it == breads.end() :
            continue
        
        it = it.next
    elif command[0] == 'D' :
        if it == breads.end() :
            continue
            
        it = breads.erase(it)
    else : 
        breads.insert(it,command[1])
    
it = breads.begin()
while it != breads.end() :
    print(it.data, end = '')
    it = it.next