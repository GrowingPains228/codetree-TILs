n,m = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

ans = 0
for i in range(n) :
    result = 0
    idx = i
    for k in range(m) :
        result += arr[idx]
        idx = arr[idx] - 1
    ans = max(ans, result)

print(ans)