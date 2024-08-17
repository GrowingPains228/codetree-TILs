import sys

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

left, right = 0, n-1
ans = sys.maxsize
while left < right:
    ans = min(ans, abs(arr[right] + arr[left]))
    if abs(arr[right]) - abs(arr[left]) >= 0:
        right -= 1
    else:
        left += 1

print(ans)