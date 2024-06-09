from sortedcontainers import SortedDict

sd = SortedDict()
n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    if arr[i] in sd:
        continue
    else:
        sd[arr[i]] = i+1

for key, value in sd.items():
    print(key, value)