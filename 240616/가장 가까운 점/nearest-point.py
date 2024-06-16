import heapq

n, m = tuple(map(int, input().split()))
pq = []
for _ in range(n):
    x,y = tuple(map(int, input().split()))
    heapq.heappush(pq, ((x+y), x, y))

for _ in range(m):
    distance, x, y = heapq.heappop(pq)
    heapq.heappush(pq, (distance + 4, x+2, y+2))

print(pq[0][1], pq[0][2])