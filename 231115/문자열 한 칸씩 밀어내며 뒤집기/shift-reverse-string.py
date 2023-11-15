string, q = tuple(input().split())
q= int(q)

for _ in range(q) :
    type_num = int(input())

    if type_num == 1 :
        string = string[1:] + string[0]
    elif type_num == 2 :
        string = string[-1] + string[:-1]
    else :
        string = string[::-1]
    
    print(string)