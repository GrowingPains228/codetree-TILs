n = int(input())
arr = list(map(int, input().split()))

def Bubble_Sort() :
    is_sorted = False
    while not is_sorted :
        is_sorted = True
        for j in range(n-1) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_sorted = False

Bubble_Sort()
for elem in arr :
    print(elem, end = " ")