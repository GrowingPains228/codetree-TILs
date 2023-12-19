n,m = tuple(map(int, input().split()))
arr = [
    tuple(map(int, input().split())) for _ in range(m)
]

cnt = 0
for i in range(m) :
    a1,b1 = arr[i]
    if a1 > b1 :
        a1,b1 = b1,a1
    
    count = 0
    for j in range(m) :
        a2,b2 = arr[j]
        if a2 > b2 :
            a2, b2 = b2, a2
        
        if a1 == a2 and b1 == b2 :
            count += 1
    
    cnt = max(cnt, count)

print(cnt)