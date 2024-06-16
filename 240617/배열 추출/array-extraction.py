import heapq

pq = []
n = int(input())

for _ in range(n):
    command = input()
    if command == '0':
        if not pq:
            print(0)
            continue
        
        print(-heapq.heappop(pq))
    else:
        heapq.heappush(pq, -int(command))