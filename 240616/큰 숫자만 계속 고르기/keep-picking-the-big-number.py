import heapq

n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

pq = []
for i in range(n):
    heapq.heappush(pq, -arr[i])

for _ in range(m):
    max_num = -heapq.heappop(pq)
    max_num -= 1
    heapq.heappush(pq, -max_num)

print(-pq[0])