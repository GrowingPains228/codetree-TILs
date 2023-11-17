n,m = tuple(map(int, input().split()))
A = list(map(int, input().split()))
 
def function_() :
    global m
    sum_number = 0

    while m != 0 :
        sum_number += A[m-1]

        if m%2 == 0 :
            m //= 2
        else :
            m -= 1

    print(sum_number)

function_()