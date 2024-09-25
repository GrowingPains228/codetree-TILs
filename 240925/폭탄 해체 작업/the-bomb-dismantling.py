import heapq

n = int(input())
bombs = list()
MAX_TIME = 0
for _ in range(n):
    score, time = tuple(map(int, input().split()))
    MAX_TIME = max(MAX_TIME, time)
    bombs.append((time, score))

bombs.sort()
pq = []
ans = 0
bomb_idx = n-1
for t in range(MAX_TIME, 0, -1):
    while bomb_idx >= 0 and bombs[bomb_idx][0] >= t:
        heapq.heappush(pq, -bombs[bomb_idx][1])
        bomb_idx -= 1

    if pq:
        ans += -heapq.heappop(pq)

print(ans)