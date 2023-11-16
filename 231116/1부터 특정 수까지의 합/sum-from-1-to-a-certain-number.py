n = int(input())

def add_range(n) :
    sum_value = 0
    for i in range(1,n+1) :
        sum_value += i
    
    return sum_value//10

return_value = add_range(n)
print(return_value)