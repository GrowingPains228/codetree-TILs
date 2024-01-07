n = int(input())
arr = list(map(int, input().split()))

def Bubble_Sort() :
    for i in range(n) :
        for j in range(n-1-i) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

Bubble_Sort()
for elem in arr :
    print(elem, end = " ")