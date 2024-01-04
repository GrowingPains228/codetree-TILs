n = int(input())
arr = list(map(int, input().split()))

def merge_sort(low, high) :
    global arr
    if high - low >= 2 :
        mid = (low + high)//2
        merge_sort(low, mid)
        merge_sort(mid, high)
        merge(low, mid, high)

def merge(low, mid, high) :
    global arr
    new_arr = []
    i,j = low, mid
    while i < mid and j < high :
        if arr[i] < arr[j] :
            new_arr.append(arr[i])
            i += 1
        else :
            new_arr.append(arr[j])
            j += 1

    while i < mid :
        new_arr.append(arr[i])
        i += 1

    while j < high :
        new_arr.append(arr[j])
        j += 1
    
    for idx in range(low, high) :
        arr[idx] = new_arr[idx-low]

merge_sort(0, len(arr))

for elem in arr :
    print(elem, end =" ")