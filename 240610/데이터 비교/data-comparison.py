n1 = int(input())
arr1 = list(map(int, input().split()))
s1 = set(arr1)

n2 = int(input())
arr2 = list(map(int, input().split()))
s2 = set(arr2)

for elem in arr2:
    if elem in s1:
        print(1, end = ' ')
    else:
        print(0, end = ' ')