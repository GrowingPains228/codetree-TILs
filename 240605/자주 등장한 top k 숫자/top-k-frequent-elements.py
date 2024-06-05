MAX_RANGE = 10**5
from collections import defaultdict
n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

d = defaultdict()

for elem in arr:
    if elem in d:
        d[elem] += 1
    else:
        d[elem] = 1

count = dict()
for key, value in d.items():
    if value in count:
        count[value].append(key)
    else:
        count[value] = [key]


for i in range(MAX_RANGE, -1, -1):
    if k == 0:
        break
    
    if i in count:
        count[i].sort(reverse=True)
        for elem in count[i]:
            print(elem, end=" ")
            k -= 1

            if k == 0:
                break