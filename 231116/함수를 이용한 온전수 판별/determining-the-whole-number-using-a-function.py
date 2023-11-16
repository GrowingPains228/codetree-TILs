a,b = tuple(map(int, input().split()))

def is_completeNumber(number) :
    if number % 2 == 0 :
        return False

    if number % 10 == 5 :
        return False

    if number % 3 == 0 and number % 9 != 0 :
        return False

    return True

cnt = 0
for i in range(a,b+1) :
    if is_completeNumber(i) :
        cnt += 1

print(cnt)