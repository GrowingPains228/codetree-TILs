import heapq

n = int(input())
arr = list(map(int, input().split()))

multiGroup = []

for elem in arr:
    heapq.heappush(multiGroup, elem)
    if len(multiGroup) < 3:
        print(-1)
        continue
    
    sum_numbers = 1
    n_Arr = []
    for _ in range(3):
        num = heapq.heappop(multiGroup)
        sum_numbers *= num
        n_Arr.append(num)
    print(sum_numbers)

    for elem in n_Arr: 
        heapq.heappush(multiGroup, elem)