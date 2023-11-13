string_arr = input().split()

sum_len  = 0
for elem in string_arr :
    sum_len += len(elem)
print(sum_len)