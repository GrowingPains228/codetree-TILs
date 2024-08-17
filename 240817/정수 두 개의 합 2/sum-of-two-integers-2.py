n, k = map(int, input().split())

arr = [0] + [int(input()) for _ in range(n)]
arr.sort()
ans = 0
j = n-1

for i in range(n, 1, -1):
    if arr[i] > k:
        continue

    while j-1 >= 1 and (arr[i] + arr[j] > k or j >= i):
        j -= 1

    if arr[i] + arr[j] <= k:
        ans += j # j 앞에 있는 모든 원소들이 모두 가능하다!

print(ans)