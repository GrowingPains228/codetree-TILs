n = int(input())

def is_oneNumber(number) :
    if number == 1 :
        return 0

    return is_oneNumber(number//2) + 1 if number % 2 == 0 else is_oneNumber(number*3 + 1) + 1

cnt = is_oneNumber(n)
print(cnt)