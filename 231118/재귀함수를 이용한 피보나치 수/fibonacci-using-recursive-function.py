def f(n) :
    if n == 1 :
        return 1
    if n == 2: 
        return 1
    
    return f(n-2) + f(n-1)

n = int(input())

print(f(n))