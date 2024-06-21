import heapq

pq = list()
n = int(input())
for _ in range(n):
    num = int(input())

    if num == 0:
        if pq:
            x,y = heapq.heappop(pq)
            print(y)
        else:
            print(0)
    else:
        heapq.heappush(pq, (abs(num), num) )