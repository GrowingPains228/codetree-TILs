binary_string = list(input())

def change_decimal(bin_str) :
    if len(bin_str) == 1 :
        return int(bin_str[0])

    return change_decimal(bin_str[:-1]) * 2 + int(bin_str[-1])

max_num = 0
for i in range(len(binary_string)) :
    if binary_string[i] != '0' :
        continue
    
    binary_string[i] = '1'
    change_num = change_decimal(binary_string)
    max_num = max(max_num, change_num)

    binary_string[i] = '0'

print(max_num)