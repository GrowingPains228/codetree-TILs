x,y = tuple(map(int, input().split()))

# 앞으로 읽어도, 뒤로 읽어도 똑같은 숫자여야함.
# reverse 를 통해서 간단히 구현 가능

ans = 0
for i in range(x,y+1) :
    num1 = list(str(i))
    num2 = reversed(num1)

    if ''.join(num1) == ''.join(num2) :
        ans += 1

print(ans)