n = int(input())
a1, b1, c1 = tuple(map(int, input().split()))
a2, b2, c2 = tuple(map(int, input().split()))

def check_combi(num1, num2, num3) :
    if min(abs(a1-num1), n-abs(a1-num1)) <= 2 and min(abs(b1-num2), n-abs(b1-num2)) <= 2 and min(abs(c1-num3), n-abs(c1-num3)) <= 2 :
        return True

    if min(abs(a2-num1), n-abs(a2-num1)) <= 2 and min(abs(b2-num2), n-abs(b2-num2)) <= 2 and min(abs(c2-num3), n-abs(c2-num3)) <= 2 :
        return True

    return False
    

cnt = 0
for i in range(1,n+1) :
    for j in range(1,n+1) :
        for k in range(1,n+1) :
            if check_combi(i,j,k) :
                cnt += 1

print(cnt)