A_str = input()

command_str = list(input())

for elem in command_str :
    if elem == 'L' :
        A_str = A_str[1:] + A_str[0]
    else :
        A_str = A_str[-1] + A_str[:-1]

print(A_str)