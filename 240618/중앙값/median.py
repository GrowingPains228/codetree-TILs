import heapq
t = int(input())

for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))

    max_pq = []
    min_pq = []
    median = arr[0]
    print(median, end = " ")

    for i in range(1,m):
        if i % 2 == 1:
            if arr[i] < median:
                heapq.heappush(max_pq, -arr[i])
            else:
                heapq.heappush(min_pq, arr[i])
        else:
            if len(max_pq) > len(min_pq):
                new_cand = -heapq.heappop(max_pq)
            else:
                new_cand = heapq.heappop(min_pq)

            nums = sorted([median, arr[i], new_cand])
            heapq.heappush(max_pq, -nums[0])
            median = nums[1]
            heapq.heappush(min_pq, nums[2])
            print(median, end = " ")

    print()