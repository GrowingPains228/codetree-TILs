MAX_RANGE = 10000
n,k = tuple(map(int, input().split()))

arr = [0] * (MAX_RANGE + 1)

for _ in range( n) :
    idx, value = tuple(input().split())
    arr[int(idx)] = 1 if value == 'G' else 2

ans = 0

for i in range(1, n - k + 2) :
    sum_value = 0
    for j in range(i, i + k + 1) :
        sum_value += arr[j]

    ans = max(ans, sum_value)

print(ans)