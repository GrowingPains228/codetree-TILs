n, m = tuple(map(int, input().split()))
num_arr = list(map(int, input().split()))
find_num = list(map(int, input().split()))
d = dict()

for num in num_arr:
    if num in d:
        cnt = d[num]
        d[num] = cnt + 1
    else:
        d[num] = 1


for elem in find_num:
    if elem in d:
        print(d[elem], end=" ")
    else:
        print(0, end=" ")