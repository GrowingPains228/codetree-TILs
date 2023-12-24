a,b = tuple(map(int, input().split()))
c,d = tuple(map(int, input().split()))

ans = 0
if a > d or b < c :
    ans = (b - a) + (d - c)
else :
    if a <= c :
        if d <= b :
            ans = b-a
        elif c <= b and b <= d :
            ans = d - a

    elif c <= a :
        if b <= d :
            ans = d - c
        elif a <= d and d <= b :
            ans = b - c
print(ans)