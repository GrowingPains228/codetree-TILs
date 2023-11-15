def print_gcd(num1, num2) :
    comman_divisor = 1
    for i in range(1,101) :
        if i > num1 or i > num2 :
            break

        if num1%i == 0 and num2%i == 0 :
            comman_divisor = i

    print(comman_divisor)

n1, n2 = tuple(map(int, input().split()))
print_gcd(n1, n2)