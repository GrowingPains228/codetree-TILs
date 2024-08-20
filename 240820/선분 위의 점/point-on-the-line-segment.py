n,m = map(int, input().split())
vertexList = list(map(int, input().split()))
vertexList.sort()


def lower_bound(arr, target):
    left, right = 0, n-1
    min_idx = n

    while left <= right:
        mid = (left+right)//2
        if arr[mid] >= target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1

    return min_idx


def upper_bound(arr, target):
    left, right = 0, n - 1
    min_idx = n

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1

    return min_idx


for _ in range(m):
    a, b = map(int, input().split())
    first_idx, second_idx = lower_bound(vertexList, a), upper_bound(vertexList, b)
    if first_idx == second_idx:
        print(0)
    else:
        print(second_idx - first_idx)