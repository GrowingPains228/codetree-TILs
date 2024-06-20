from sortedcontainers import SortedSet

n,m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
s = SortedSet()

ans = 0
for elem in arr:
    if elem == 1 and 1 in s:
        break
    
    for i in range(elem):
        if elem-i not in s:
            s.add(elem-i)
            ans += 1
            break

print(ans)