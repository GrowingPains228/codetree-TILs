import heapq
n = int(input())
MAX_T = 0

bumbList = []
for _ in range(n):
    (score, time_limit) = tuple(map(int, input().split()))
    MAX_T = max(MAX_T, time_limit)
    bumbList.append((time_limit, score))


bumbList.sort()

pq = []
bomb_idx = n - 1
ans = 0

for t in range(MAX_T, 0, -1):
    while bomb_idx >= 0 and bumbList[bomb_idx][0] >= t:
        heapq.heappush(pq, -bumbList[bomb_idx][1])
        bomb_idx -= 1
    
    if pq:
        ans += - heapq.heappop(pq)

print(ans)