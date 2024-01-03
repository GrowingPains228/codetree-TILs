n = int(input())
arr = list(map(int, input().split()))

def insertion_sort(arr) :
    length = len(arr)
    for i in range(1, length) :
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key :
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
    
    return arr

insertion_sort(arr)

for elem in arr :
    print(elem, end = " ")