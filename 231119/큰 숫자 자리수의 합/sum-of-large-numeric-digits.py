arr = list(map(int, input().split()))

def function(number) :
    if number < 10 :
        return number

    return function(number//10) + number%10

multinum = 1
for elem in arr :
    multinum *= elem
    
print(function(multinum))