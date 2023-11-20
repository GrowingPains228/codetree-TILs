n = int(input())
arr = list(map(int, input().split()))
arr.sort()

for elem in arr :
    print(elem, end = " ")
print()

for elem in arr[::-1] :
    print(elem, end = " ")