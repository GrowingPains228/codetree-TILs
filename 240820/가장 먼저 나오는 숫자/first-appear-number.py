n, m = map(int, input().split())
arr = list(map(int, input().split()))
targetList = list(map(int, input().split()))


def lower_bound(arr, target):
    left, right = 0, n-1
    min_idx = n
    while left <= right:
        mid = (left + right)//2
        if arr[mid] >= target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1

    return min_idx


for elem in targetList:
    min_idx = lower_bound(arr, elem)
    if arr[min_idx] == elem:
        print(min_idx+1)
    else:
        print(-1)