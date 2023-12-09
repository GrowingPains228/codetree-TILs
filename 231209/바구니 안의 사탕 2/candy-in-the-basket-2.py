MAX_RANGE = 100
n, k = tuple(map(int, input().split()))

arr = [0] * (MAX_RANGE +1)

for _ in range(n) :
    nums, idx = tuple(map(int, input().split()))
    arr[idx] += nums

ans = 0
if k >= (MAX_RANGE//2) :
    for i in range(1, MAX_RANGE + 1 ) :
        nums_sum = sum(arr[i : i + 2*k + 1])
        ans = max(nums_sum, ans)
else :
    for i in range(1, (MAX_RANGE + 1) - 2*k ) :
        nums_sum = sum(arr[i : i + 2*k + 1])
        ans = max(nums_sum, ans)

print(ans)