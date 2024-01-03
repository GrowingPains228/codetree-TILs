n = int(input())
arr = list(map(int, input().split()))

while True :
    sorted = True
    for i in range(n-1) :   
        if arr[i] > arr[i+1] :
            arr[i], arr[i+1] = arr[i+1], arr[i]
            sorted = False
    
    if sorted :
        break

for elem in arr :
    print(elem, end=' ')