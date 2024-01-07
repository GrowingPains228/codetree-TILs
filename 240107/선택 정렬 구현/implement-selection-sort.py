n = int(input())
arr = list(map(int, input().split()))

def Selection_Sort() :
    for i in range(n) :
        min_num = i
        for j in range(i + 1, n) :
            if arr[min_num] > arr[j] :
                min_num = j
            
        arr[min_num], arr[i] = arr[i], arr[min_num]

Selection_Sort()

for elem in arr :
    print(elem, end = " ")