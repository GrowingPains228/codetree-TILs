MAX_LINE = 1000
T,a,b = tuple(map(int, input().split()))

arr = [''] * (MAX_LINE + 1)
unique_arr = [True] * (MAX_LINE + 1)
for _ in range(T) :
    alpha, position = tuple(input().split())
    arr[int(position)] = alpha

cnt = 0
for i in range(0,MAX_LINE+1) :
    if arr[i] == '' :
        continue
    
    alpha1 = arr[i]
    for j in range(i+1, MAX_LINE+1) :
        if arr[j] == '' or arr[j] == alpha1 :
            continue
        
        alpha2 = arr[j]

        start, end = 0,0
        if alpha1 == 'S' :
            start, end = (i+j)//2, i
        else :
            start, end = j, (i+j)//2 if (i+j) % 2 == 0 else (i+j)//2 + 1

        for k in range(start, end-1, -1) :
            unique_arr[k] = True

        break

print(sum(unique_arr[a:b+1]))