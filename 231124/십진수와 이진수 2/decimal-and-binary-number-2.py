N = list(map(int,list(input())))

def return_Decimal(arr) :
    sum_n = 0
    for elem in arr :
        sum_n = sum_n * 2 + elem

    return sum_n

def return_Digit(number) :
    arr = []
    while True :
        if number < 2:
            arr.append(number)
            break
    
        arr.append(number%2)
        number //= 2
    return arr

first_digit = return_Decimal(N)

first_digit *= 17
digits = return_Digit(first_digit)

for digit in digits[::-1] :
    print(digit, end="")