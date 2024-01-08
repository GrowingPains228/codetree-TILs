n = int(input())
arr = list(map(int, input().split()))
Merge_arr = [0] * n

def Merge_Sort(low, high) :
    if low < high :
        mid = (low + high)//2
        
        Merge_Sort(low, mid)
        Merge_Sort(mid + 1, high)
        Merge(low, mid, high)

def Merge(low, mid, high) :
    i,j = low, mid+1
    k = low
    while i <= mid and j <= high :
        if arr[i] < arr[j] :
            Merge_arr[k] = arr[i]
            i += 1
        else :
            Merge_arr[k] = arr[j]
            j += 1

        k += 1
    
    while i <= mid :
        Merge_arr[k] = arr[i]
        i += 1
        k += 1
    
    while j <= high :
        Merge_arr[k] = arr[j]
        j += 1
        k += 1
    
    for idx in range(low, k) :
        arr[idx] = Merge_arr[idx]
    
Merge_Sort(0,n-1)

for elem in arr :
    print(elem, end = " ")