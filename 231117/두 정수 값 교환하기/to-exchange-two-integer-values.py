a,b = tuple(map(int, input().split()))

def swap(a,b) :
    a,b = b,a
    return a,b

a,b = swap(a,b) 
print(a,b)