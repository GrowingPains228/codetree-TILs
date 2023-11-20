n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

arr.sort()
print(arr[k-1])