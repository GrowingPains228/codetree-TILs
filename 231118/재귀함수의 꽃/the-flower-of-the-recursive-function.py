n = int(input())

def print_number(number) :
    global n
    if number == 0 or number == n+1 :
        return

    print(number, end = " ")
    print_number(number-1)
    print(number, end = " ")

print_number(n)