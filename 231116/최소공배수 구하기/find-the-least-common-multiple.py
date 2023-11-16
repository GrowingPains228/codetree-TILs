n,m = tuple(map(int, input().split()))

def find_lcm(n,m) :
    ldm = 1
    temp_n = n
    temp_m = m
    #공약수로 나눠서 구하는 방식
    for i in range(1, min(n,m) +1) :
        if n%i == 0 and m%i == 0:
            ldm *= i
            temp_n //= i
            temp_m //= i

    #공약수의 배수중 최소공배수가 존재.
    cnt = 1
    while True :
        if (ldm * cnt) % n == 0 and (ldm * cnt) % m == 0 :
            print(ldm)
            break
        else :
            cnt += 1

find_lcm(n,m)