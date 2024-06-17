import heapq
pq = []

n = int(input())
arr = list(map(int, input().split()))
for elem in arr:
    heapq.heappush(pq, -elem)

while len(pq) >= 2:
    x = -heapq.heappop(pq)
    y = -heapq.heappop(pq)
    if x == y :
        continue
        
    heapq.heappush(pq, -(x-y))

print(-pq[0] if pq else -1)