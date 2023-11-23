n, B = tuple(map(int, input().split()))

digits = []
while True :
    if n < B :
        digits.append(n)
        break
    
    digits.append(n % B)
    n //= B
    
for elem in digits[::-1] :
    print(elem, end = "")