string = input()
arr = list(string)

while len(string) > 1 :
    index = int(input())

    if index >= len(arr) :
        arr.pop(len(arr)-1)
    else :
        arr.pop(index)
    
    string = ''.join(arr)
    print(string)