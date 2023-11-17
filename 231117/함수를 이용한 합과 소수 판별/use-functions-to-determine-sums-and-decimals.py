a,b = tuple(map(int, input().split()))

#소수점 판별 함수
def is_prime_num(number) :
    if number == 1 :
        return False

    for i in range(2, number) :
        if number%i == 0 :
            return False

    return True

#모든 자릿수의 합이 짝수인 수
def is_allNum(number) :
    if number < 10 :
        return number%2 == 0
    elif number == 100 :
        return False
    
    return (number//10 + number%10)%2 == 0

cnt = 0
for i in range(a,b+1) :
    if is_prime_num(i) and is_allNum(i) :
        cnt += 1

print(cnt)