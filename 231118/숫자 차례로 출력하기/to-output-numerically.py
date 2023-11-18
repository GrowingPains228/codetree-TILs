n = int(input())

def order_function(n) :
    if n == 0 :
        return
    
    order_function(n-1)
    print(n, end = " ")

def reverce_functino(n) :
    if n == 0 :
        return 
    
    print(n, end = " ")
    reverce_functino(n-1)

order_function(n)
print()
reverce_functino(n)