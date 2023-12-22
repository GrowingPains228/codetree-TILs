#언덕의 개수 입력 받기
n = int(input())
arr = [
    int(input()) for _ in range(n)
]

arr.sort()
ans = 0
if n >= 2 :
    if arr[-1] - arr[0] > 17 :
        # 총 높거나 낮아져야 할 비용
        cost = (arr[-1] - arr[0] - 17)
        cost1, cost2 = cost//2, cost - cost//2
        ans = cost1 * cost1 + cost2 * cost2

print(ans)