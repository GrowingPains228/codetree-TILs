arr = list(map(int, input().split()))

min_num = arr[0]
max_num = arr[0]

for i in range(1,len(arr)) :
    if arr[i] in (-999, 999) :
        break

    if arr[i] <= min_num :
        min_num = arr[i]
    
    if arr[i] >= max_num :
        max_num = arr[i]

print(max_num, min_num)