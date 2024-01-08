n = int(input())
arr = list(map(int, input().split()))

def partition(low, high) :
    pivot = high
    i = low-1
    for j in range(low, high) :
        if arr[j] < arr[pivot] :
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    i += 1
    arr[pivot], arr[i] = arr[i], arr[pivot]
    return i


def Quick_Sort(low, high) :
    if low < high :
        mid = partition(low, high)

        Quick_Sort(low, mid-1)
        Quick_Sort(mid+1, high)


Quick_Sort(0, n-1)

for elem in arr :
    print(elem, end = " ")