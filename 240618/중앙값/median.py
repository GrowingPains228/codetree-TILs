import heapq
t = int(input())

for _ in range(t):
    cur_pop_max = []
    m = int(input())
    arr = list(map(int, input().split()))
    pq = []
    heapq.heappush(pq, arr[0])
    print(pq[0], end = " ")
    for i in range(1, m):
        heapq.heappush(pq, arr[i])
        if i%2 == 0:
            popitem = heapq.heappop(pq)
            heapq.heappush(cur_pop_max, -popitem)
            if - cur_pop_max[0] > pq[0]:
                tmp = heapq.heappop(pq)
                heapq.heappush(pq, -heapq.heappop(cur_pop_max))
                heapq.heappush(cur_pop_max, -tmp)
                print(pq[0], end = " ")
            else:
                print(pq[0], end = " ")
    print()