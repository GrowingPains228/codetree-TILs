arr = list(map(int, input().split()))

arr_down500 = []
arr_up500 = []

for elem in arr :
    if elem > 500 :
        arr_up500.append(elem)
    else :
        arr_down500.append(elem)

max_num = -1
for i in arr_down500 :
    if max_num <= i :
        max_num = i
print(max_num, end = " ")

max_num = 1001
for i in arr_up500 :
    if max_num >= i :
        max_num = i
print(max_num)