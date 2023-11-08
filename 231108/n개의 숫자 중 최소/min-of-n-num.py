n = int(input())
arr = list(map(int, input().split()))

min_num = arr[0]

for elem in arr:
    if min_num >= elem :
        min_num = elem

cnt = 0
for i in arr:
    if i == min_num :
        cnt += 1
print(min_num, cnt)