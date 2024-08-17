import sys

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

left, right = 0, n-1
ans = sys.maxsize
ans = min(ans, abs(arr[right] + arr[left]))
while left < right:
    if arr[right] - arr[left] >= 0:
        right -= 1
    else:
        left += 1

    ans = min(ans, abs(arr[right] + arr[left]))

print(ans)