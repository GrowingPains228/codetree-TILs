n,m = tuple(map(int, input().split()))

def find_lcm(n,m) :
    ldm = 1
    temp_n = n
    temp_m = m
    #공약수로 나눠서 구하는 방식
    i = 2
    while min(temp_n, temp_m) >= i :
        if temp_m % i == 0 and temp_n % i == 0 :
            temp_n //= i
            temp_m //= i
            ldm *= i
            i = 2
            
        i += 1

    print(temp_m * temp_n * ldm)

find_lcm(n,m)