import heapq

n = int(input())
nums = list(map(int, input().split()))
hq = []
for num in nums:
    heapq.heappush(hq, num)
ans = 0

while len(hq) >= 2:
    num1 = heapq.heappop(hq)
    num2 = heapq.heappop(hq)
    new_num = num1 + num2
    ans += new_num
    heapq.heappush(hq, new_num)

print(ans)