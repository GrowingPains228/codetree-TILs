# 오름차순으로 정렬된 배열에서
# 앞에서부터 K+1를 삭제한 후,
# 평균을 구하면 끝.
import heapq
import statistics

n = int(input())
arr = list(map(int, input().split()))

ans = 0
total = sum(arr)
length = len(arr)
pq = []

for k in range(n-2, 0, -1):
    diff = total - sum(arr[:k])
    new_arr = sorted(arr[k::])
    heapq.heappush(pq, (-(diff-new_arr[0])/(length-k-1)))

ans = -pq[0]

print(f"{ans:0.2f}")