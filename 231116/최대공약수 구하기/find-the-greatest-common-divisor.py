def print_gcd(num1, num2) :
    comman_divisor = 1
    for i in range(1,50) :
        if num1%i != 0 or num2%i != 0 :
            print(comman_divisor)
            break

        num1 //= i
        num2 //= i
        comman_divisor *= i

n1, n2 = tuple(map(int, input().split()))
print_gcd(n1, n2)