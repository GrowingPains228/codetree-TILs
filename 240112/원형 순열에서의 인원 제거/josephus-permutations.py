from collections import deque

class Queue : 
    def __init__(self) :
        self.dq = deque()

    def push(self,item) :
        self.dq.append(item)
    
    def empty(self) :
        return not self.dq
    
    def size(self) :
        return len(self.dq)
    
    def pop(self) :
        if self.empty() :
            raise Exception("Queue is empty")

        return self.dq.popleft()
    
    def front(self) :
        if self.empty() :
            raise Exception("Queue is empty")
        
        return self.dq[0]

n,k = tuple(map(int, input().split()))
dq = Queue()
for i in range(1,n+1) :
    dq.push(i)

for i in range(n) :
    for j in range(k-1) :
        dq.push(dq.front())
        dq.pop()
    
    print(dq.pop(), end = " ")