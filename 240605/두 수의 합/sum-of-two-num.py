n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
d = dict()

for elem in arr:
    if elem in d:
        d[elem] = d[elem] + 1
    else:
        d[elem] = 1

ans = 0
for elem in arr:
    if elem in d:
        d[elem] = d[elem] - 1

    if (k - elem) in d and d[k - elem] != 0:
        d[k - elem] = d[k - elem] - 1
        ans += 1

print(ans)