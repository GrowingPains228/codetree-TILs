N = int(input())

def callu_func(n) :
    if n == 1 :
        return 1
    elif n == 2 :
        return 2
    
    return callu_func(n//3) + callu_func(n-1)

print(callu_func(N))