n = int(input())
pass1, pass2, pass3 = tuple(map(int, input().split()))

def in_range(n1, n2, n3) :
    if pass1 - 2 <= n1 and n1 <= pass1 + 2 :
        return True
    
    if pass2 - 2 <= n2 and n2 <= pass2 + 2 :
        return True

    if pass3 - 2 <= n3 and n3 <= pass3 + 2 :
        return True
    
    return False

cnt = 0
for i in range(1,n+1) :
    for j in range(1,n+1) :
        for k in range(1, n+1) :
            if in_range(i, j, k) :
                cnt += 1

print(cnt)