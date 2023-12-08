n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

ans = 0
for i in range(n - k + 1) :
    group_sum = 0

    for j in range(i, i + k) :
        group_sum += arr[j]
    
    ans = max(ans, group_sum)

print(ans)