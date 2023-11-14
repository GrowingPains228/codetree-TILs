string = list(input())

while len(string) > 1 :
    index = int(input())

    if index >= len(string) :
        string.pop(len(string)-1)
    else :
        string.pop(index)
    
    for elem in string :
        print(elem, end = "")
    print()