n,m = tuple(map(int, input().split()))

def gcd(n1, n2) :
    gcd_num = 0
    for i in range(1, min(n1, n2) +1) :
        if n1 % i == 0 and n2 % i == 0 :
            gcd_num = i
    return gcd_num

def lcm(n1,n2) :
    return n1 * n2 // gcd(n1,n2)

print(lcm(n, m))