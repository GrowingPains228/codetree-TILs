import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, item):
        heapq.heappush(self.items, -item)

    def size(self):
        return len(self.items)

    def empty(self):
        return not self.items

    def pop(self):
        if self.empty():
            raise Exception("PriorityQueue is Empty")
        return -heapq.heappop(self.items)

    def top(self):
        if self.empty():
            raise Exception("PriorityQueue is Empty")

        return -self.items[0]


n = int(input())
ph = PriorityQueue()
for _ in range(n):
    string = input().split()
    if string[0] == "push":
        ph.push(int(string[1]))
    elif string[0] == "size":
        print(ph.size())
    elif string[0] == "empty":
        print(int(ph.empty()))
    elif string[0] == "pop":
        print(int(ph.pop()))
    else:
        print(int(ph.top()))