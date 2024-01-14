from collections import deque

class Queue :
    def __init__(self) :
        self.dq = deque()

    def empty(self) :
        return not self.dq
    
    def push(self, item) :
        self.dq.append(item)
    
    def pop(self) :
        if self.empty() :
            raise Exception("Queue is empty")
    
        return self.dq.popleft()

    def front(self) :
        if self.empty() :
            raise Exception("Queue is empty")
        
        return self.dq[0]
    
    def size(self) :
        return len(self.dq)

n = int(input())
q = Queue()
for _ in range(n) :
    command = input()

    if command.startswith("push") :
        q.push(command.split()[1])
    elif command == "front" :
        print(q.front())
    elif command == "pop" :
        print(q.pop())
    elif command == "size" :
        print(q.size())
    else :
        print(int(q.empty()))