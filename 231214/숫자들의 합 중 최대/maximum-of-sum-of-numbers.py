x,y = tuple(map(int, input().split()))

ans = 0
for i in range(x, y+1) :
    result = 0
    while i > 0 :
        result += i%10
        i //= 10
    ans = max(ans, result)

print(ans)