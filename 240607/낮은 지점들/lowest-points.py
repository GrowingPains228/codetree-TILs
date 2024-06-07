n = int(input())
dot_list = list()
d = dict()
for _ in range(n):
    (x, y) = tuple(map(int, input().split()))
    dot_list.append((x,y))

dot_list.sort(key = lambda x : x[1])
ans = 0
for (x, y) in dot_list:
    if x in d:
        continue
    
    d[x] = y
    ans += y


print(ans)