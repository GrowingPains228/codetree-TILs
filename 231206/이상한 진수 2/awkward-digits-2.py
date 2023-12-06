binary_string = list(map(int, list(input())))

def change_decimal(bin_str) :
    if len(bin_str) == 1 :
        return bin_str[0]

    return change_decimal(bin_str[:-1]) * 2 + bin_str[-1]

max_num = 0
for i in range(len(binary_string)) :
    binary_string[i] = binary_string[i] ^ 1
    change_num = change_decimal(binary_string)
    max_num = max(max_num, change_num)

    binary_string[i] = binary_string[i] ^ 1

print(max_num)