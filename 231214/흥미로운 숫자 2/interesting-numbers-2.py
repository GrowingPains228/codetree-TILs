x,y = tuple(map(int, input().split()))

ans = 0

for i in range(x, y+1) :
    num = i
    digit = [0] * 10
    all_digit = 0

    while num > 0 :
        digit[num%10] += 1
        all_digit += 1
        num //= 10
    
    interesting = False

    for j in range(10) :
        if digit[j] == all_digit -1 :
            interesting = True
            break
    
    if interesting :
        ans += 1

print(ans)