n = int(input())
arr = list(map(int, input().split()))

def partition(low, high) :
    pivot = arr[high]
    i = low -1
    for j in range(low, high) :
        if arr[j] < pivot :
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

def quick_sort(low, high) :
    if low < high :
        pos = partition(low, high)

        quick_sort(low, pos -1)
        quick_sort(pos +1, high)

quick_sort(0, n-1)

for elem in arr :
    print(elem, end = " ")