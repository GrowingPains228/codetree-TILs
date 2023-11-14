string = list(input())

char = string[1]


for i in range(len(string)) :
    if string[i] == char :
        string[i] = string[0]
print(''.join(string))