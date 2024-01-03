n = int(input())
arr = list(map(int, input().split()))

for i in range(n-1) :
    min = i
    for j in range(i+1, n) :
        if arr[j] < arr[min] :
            min = j
    
    arr[i], arr[min] = arr[min], arr[i]

for elem in arr :
    print(elem, end = " ")