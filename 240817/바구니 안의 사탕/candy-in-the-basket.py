AXIS_SIZE = 1000000
n, k = map(int, input().split())

# prexible_Sum 을 구한다.
prexible_sum = [0] * (AXIS_SIZE + 1)
for _ in range(n):
    value, x = tuple(map(int, input().split()))
    prexible_sum[x] += value

for i in range(1, AXIS_SIZE+1):
    prexible_sum[i] += prexible_sum[i-1]

ans = 0
if k >= AXIS_SIZE/2:
    ans = prexible_sum[AXIS_SIZE]
else:
    ans = prexible_sum[k]
    for c in range(k+1, AXIS_SIZE+1-k):
        ans = max(ans, prexible_sum[c+k] - prexible_sum[c-k-1])

print(ans)