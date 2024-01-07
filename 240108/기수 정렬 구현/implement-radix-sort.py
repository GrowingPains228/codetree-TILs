MAX_LENGTH = 6
n = int(input())
arr = list(map(int, input().split()))

# k is length of number
def Radix_sort(k) :
    global arr
    for pos in range(k) :
        digit_arr = [[] for _ in range(10)]
        for elem in arr :
            digit = (elem//(10 ** pos))%10
            digit_arr[digit].append(elem)
        
        storage_arr = []
        for i in range(10) :
            for j in range(len(digit_arr[i])) :
                storage_arr.append(digit_arr[i][j])
        
        arr = storage_arr[::]

Radix_sort(MAX_LENGTH)

for elem in arr :
    print(elem, end = " ")