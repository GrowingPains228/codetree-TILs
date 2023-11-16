a,b = tuple(map(int, input().split()))

def is_prime(number) :
    for i in range(2, number) :
        if number % i == 0 :
            return False
    
    return True

cnt = 0

for i in range(a,b+1) :
    if i > 1 and is_prime(i) :
        cnt += i

print(cnt)