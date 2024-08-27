import heapq
n, t_max = tuple(map(int, input().split()))
d = [int(input()) for _ in range(n)]


def is_possible(k):
    pq = []
    for i in range(k):
        heapq.heappush(pq, d[i])

    for i in range(k, n):
        cur_time = heapq.heappop(pq)

        heapq.heappush(pq, cur_time + d[i])

    end_time = 0
    while pq:
        end_time = max(end_time, heapq.heappop(pq))

    return end_time <= t_max


left = 1
right = n
ans = n

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)