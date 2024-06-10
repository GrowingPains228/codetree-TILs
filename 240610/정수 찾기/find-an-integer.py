n1 = int(input())
arr1 = list(map(int, input().split()))

n2 = int(input())
arr2 = list(map(int, input().split()))

s = set(arr1)

for elem in arr2:
    if elem in s:
        print(1)
    else:
        print(0)