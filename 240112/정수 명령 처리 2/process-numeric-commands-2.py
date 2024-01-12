from collections import deque

class Queue :
    def __init__(self) :
        self.dq = deque()
    
    def push(self, item) :
        self.dq.append(item)
        
    def empty(self) :
        return not self.dq
    
    def size(self) :
        return len(self.dq)
    
    def front(self) :
        if self.empty() :
            raise Exception("Queue is empty")
        
        return self.dq[0]
    
    def pop(self) :
        if self.empty() :
            raise Exception("Queue is empty")
        
        return self.dq.popleft()
    
n = int(input())
dq = Queue()
for _ in range(n) :
    command = input()

    if command.startswith("push") :
        dq.push(command.split()[1])
    elif command == "front" :
        print(dq.front())
    elif command == "size" :
        print(dq.size())
    elif command == "empty" :
        print(int(dq.empty()))
    elif command == "pop" :
        print(dq.pop())