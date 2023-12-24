a,b = tuple(map(int, input().split()))
c,d = tuple(map(int, input().split()))

ans = 0
if a > d or b < c :
    ans = (b - a) + (d - c)
else :
    ans = max(b,d) - min(a,c)
print(ans)