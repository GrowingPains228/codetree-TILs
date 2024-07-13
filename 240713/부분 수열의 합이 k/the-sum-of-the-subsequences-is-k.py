n,k = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))
prefix_sum  = [0] * (n+1)
ans = 0


def get_sum(s, e):
    return prefix_sum[e] - prefix_sum[s-1]


prefix_sum[0] = 0
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]


for i in range(1, n+1):
    for j in range(i, n+1):
        if get_sum(i, j) == k:
            ans += 1

print(ans)