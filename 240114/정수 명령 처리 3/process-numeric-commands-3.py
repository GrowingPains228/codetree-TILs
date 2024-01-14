from collections import deque

class Deque :
    def __init__(self) :
        self.dq = deque()

    def empty(self) :
        return not self.dq
    
    def push_back(self, item) :
        self.dq.append(item)

    def push_front(self, item) :
        self.dq.appendleft(item)
    
    def pop_front(self) :
        if self.empty() :
            raise Exception("Queue is empty")
    
        return self.dq.popleft()

    def pop_back(self) :
        if self.empty() :
            raise Exception("Queue is empty")
    
        return self.dq.pop()

    def front(self) :
        if self.empty() :
            raise Exception("Queue is empty")
        
        return self.dq[0]

    def back(self) :
        if self.empty() :
            raise Exception("Queue is empty")
        
        return self.dq[-1]
    
    def size(self) :
        return len(self.dq)

n = int(input())
dq = Deque()
for _ in range(n) :
    command = input()

    if command.startswith("push_back") :
        dq.push_back(command.split()[1])
    elif command.startswith("push_front") :
        dq.push_front(command.split()[1])
    elif command == "pop_back" :
        print(dq.pop_back())
    elif command == "pop_front" :
        print(dq.pop_front())
    elif command == "size" :
        print(dq.size())
    elif command == "empty" :
        print(int(dq.empty()))
    elif command == "front" :
        print(dq.front())
    else : 
        print(dq.back())