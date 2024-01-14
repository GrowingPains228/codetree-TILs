from collections import deque

class Queue :
    def __init__(self) :
        self.dq = deque()
    
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
    
    def push(self, item) :
        self.dq.append(item)
    

n, k = tuple(map(int, input().split()))
q = Queue()
for i in range(1, n+1) :
    q.push(i)

for _ in range(n) :
    for _ in range(k-1) :
        q.push(q.front())
        q.pop()

    print(q.pop(), end = " ")