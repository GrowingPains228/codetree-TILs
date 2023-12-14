MAX_LINE = 1000
T,a,b = tuple(map(int, input().split()))

arr = [''] * (MAX_LINE + 1)
for _ in range(T) :
    alpha, position = tuple(input().split())
    arr[int(position)] = alpha

cnt = 0
for i in range(a,b+1) :
    if arr[i] == '' :
        continue
    
    alpha1 = arr[i]
    for j in range(i+1, b+1) :
        if arr[j] == '' or arr[j] == alpha1 :
            continue
        
        alpha2 = arr[j]

        start, end = 0,0
        if alpha1 == 'S' :
            start, end = (i+j)//2, i
        else :
            start, end = j, (i+j)//2 if (i+j) % 2 == 0 else (i+j)//2 + 1

        for _ in range(start, end-1, -1) :
            cnt += 1

        break

print(cnt)