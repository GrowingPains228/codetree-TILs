n = int(input())
arr = list(map(int, input().split()))

idx = n-2
while idx >= 0 and arr[idx] < arr[idx + 1] :
    idx -= 1

print(idx + 1)