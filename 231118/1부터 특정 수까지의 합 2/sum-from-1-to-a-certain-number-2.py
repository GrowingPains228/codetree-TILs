n = int(input())

def add_range(n) :
    if n == 1:
        return 1
    
    return add_range(n-1) + n

print(add_range(n))