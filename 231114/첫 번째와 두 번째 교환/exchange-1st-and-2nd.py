string = list(input())

first = string[0]
second = string[1]

for i in range(len(string)) :
    if string[i] == first :
        string[i] = second
    elif string[i] == second :
        string[i] = first

    
print(''.join(string))