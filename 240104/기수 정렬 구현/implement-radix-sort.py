MAX_K = 6
MAX_DIGIT = 10

n = int(input())
arr = list(map(int, input().split()))

def sort_radix() :
    global arr

    p = 1
    for pos in range(MAX_K) :
        arr_new = [ [] for _ in range(MAX_DIGIT) ]
        for elem in arr :
            digit = (elem // p) % 10
            arr_new[digit].append(elem)
        
        arr = []
        for digit in range(MAX_DIGIT) :
            for elem in arr_new[digit] :
                arr.append(elem)
        
        p *= 10


sort_radix()

for elem in arr :
    print(elem, end = " ")