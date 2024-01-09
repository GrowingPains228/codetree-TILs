n = int(input())
arr = [0] + list(map(int, input().split()))

def heapify(n, i) :
    l,r = i*2, i*2 +1
    largest = i

    if l <= n and  arr[largest] < arr[l] :
        largest = l
    
    if r <= n and arr[largest] < arr[r] :
        largest = r
    
    if largest != i :
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(n, largest)

def heap_sort(n) :
    for i in range(n//2, 0, -1) :
        heapify(n,i)
    
    for i in range(n, 1, -1) :
        arr[1], arr[i] = arr[i], arr[1]
        heapify(i-1, 1)

heap_sort(n)

for i in range(n+1) :
    if i == 0 :
        continue
    
    print(arr[i], end = " ")