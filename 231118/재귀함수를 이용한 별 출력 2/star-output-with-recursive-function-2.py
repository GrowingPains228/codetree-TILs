n = int(input())

def start_function(n) :
    if n == 0 :
        return
    
    print("* "*n)
    start_function(n-1)
    print("* "*n)

start_function(n)