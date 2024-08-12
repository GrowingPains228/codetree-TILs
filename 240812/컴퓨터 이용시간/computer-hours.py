import heapq

n = int(input())

segments = [tuple(map(int, input().split())) for _ in range(n)]

# 각 사람별로 할당된 컴퓨터 번호를 관리한다.
assigned_nums = [0] * n

computers = list()
for i in range(1, n+1):
    heapq.heappush(computers, i)

points = list()
for i, (a, b) in enumerate(segments):
    points.append((a, 1, i))
    points.append((b, -1, i))

points.sort()

for x, v, index in points:
    if v == 1:
        assigned_nums[index] = heapq.heappop(computers)
    else:
        heapq.heappush(computers, assigned_nums[index])

for elem in assigned_nums:
    print(elem, end =' ')