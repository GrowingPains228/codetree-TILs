import sys

a,o,c = tuple(input().split())
a,c = map(int, (a,c))

def add_num(a,c) :
    return a + c

def subtraction(a,c) :
    return a - c

def multi(a,c) :
    return a * c

def division(a,c) :
    return int(a/c)

result = 0
if o == '+' :
    result = add_num(a,c)
elif o == '-' :
    result = subtraction(a,c)
elif o == '*' :
    result = multi(a,c)
elif o == '/' :
    result = division(a,c)
else : 
    result = False

print(f"{a} {o} {c} = {result}" if result != False else result)