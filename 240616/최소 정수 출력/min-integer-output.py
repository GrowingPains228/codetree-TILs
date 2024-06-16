import heapq
n = int(input())
group = []
for _ in range(n):
    x = input()

    if x == '0':
        if not group:
            print(0)
            continue
        
        print(heapq.heappop(group))
    else:
        heapq.heappush(group, int(x))