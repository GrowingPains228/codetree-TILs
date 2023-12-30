arr = list(map(int, input().split()))
arr.sort()
a,b,c = arr[0], arr[1], arr[2]
d = arr[-1] - a - b - c
print(a,b,c,d)