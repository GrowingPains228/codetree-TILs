N = int(input())
arr = list(map(int, input().split()))

def division_even(arr) : 
    for i in range(len(arr)) :
        if arr[i] % 2 == 0 : 
            arr[i] //= 2

division_even(arr)
for elem in arr :
    print(elem, end = " ")