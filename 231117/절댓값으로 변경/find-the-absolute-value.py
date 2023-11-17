N = int(input())
arr = list(map(int, input().split()))

def abs_func(arr) :
    for i in range(N) :
        if arr[i] > 0 :
            continue

        arr[i] = abs(arr[i])

abs_func(arr)
for elem in arr :
    print(elem, end = " ")