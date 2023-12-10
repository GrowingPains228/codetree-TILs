n = int(input())
pass1, pass2, pass3 = tuple(map(int, input().split()))

cnt = 0
for i in range(1,n+1) :
    for j in range(1,n+1) :
        for k in range(1, n+1) :
            if abs(pass1-i) <= 2 or abs(pass2-j) <= 2 or abs(pass3-k) <= 2 :
                cnt += 1

print(cnt)