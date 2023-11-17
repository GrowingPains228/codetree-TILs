a,b = tuple(map(int, input().split()))

def up_down(num1,num2) :
    if num1 >= num2 :
        num1 *= 2
        num2 += 10
    else :
        num2 *= 2
        num1 += 10

    return num1, num2
a,b = up_down(a,b)
print(a,b)