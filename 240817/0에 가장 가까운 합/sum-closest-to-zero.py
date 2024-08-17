import sys

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = sys.maxsize
j = n - 1
for i in range(n):
    while j >= 0 and abs(arr[i]) < abs(arr[j]):
        ans = min(ans, arr[j] + arr[i])
        j -= 1

    if j <= i:
        break

    ans = min(ans, abs(arr[j] + arr[i]))

print(ans)