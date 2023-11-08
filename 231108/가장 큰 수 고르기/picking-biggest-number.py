arr = list(map(int, input().split()))

max_num = arr[0]
for elem in arr[1::] :
    if max_num < elem :
        max_num = elem
print(max_num)