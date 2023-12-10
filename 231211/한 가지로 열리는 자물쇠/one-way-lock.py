n = int(input())
pass1, pass2, pass3 = tuple(map(int, input().split()))

def in_range(n1, n2, n3) :
    if abs(pass1-n1) <= 2 :
        return True
    
    if abs(pass2-n2) <= 2 :
        return True

    if abs(pass3-n3) <= 2 :
        return True
    
    return False

cnt = 0
for i in range(1,n+1) :
    for j in range(1,n+1) :
        for k in range(1, n+1) :
            if in_range(i, j, k) :
                cnt += 1

print(cnt)