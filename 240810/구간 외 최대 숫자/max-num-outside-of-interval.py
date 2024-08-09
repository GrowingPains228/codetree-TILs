n, q = map(int, input().split())
nums = list(map(int, input().split()))

L = [0] * n
R = [0] * n

L[0] = nums[0]
for i in range(1, n):
    L[i] = max(nums[i], L[i-1])


R[-1] = nums[-1]
for i in range(n-2, -1, -1):
    R[i] = max(nums[i], R[i+1])

for _ in range(q):
    x1, x2 = map(int, input().split())
    print(max(L[x1-2], R[x2]))