MAX_LINE = 1000
T,a,b = tuple(map(int, input().split()))

arr = [''] * (MAX_LINE + 1)
unique_arr = [False] * (MAX_LINE + 1)
for _ in range(T) :
    alpha, position = tuple(input().split())
    arr[int(position)] = alpha

cnt = 0
for i in range(1,MAX_LINE+1) :
    if arr[i] == '' :
        continue
    # S,N을 만날것이고,
    for j in range(i+1, MAX_LINE+1) :
        if arr[j] == '' :
            continue
        
        # 가까운 위치에 똑같은 놈이 있으면, 이 for문을 빠져나가서
        # 방금 그놈을 잡도록 한다.
        if arr[j] == arr[i] :
            for z in range(i,j + 1) :
                unique_arr[z] = True
            break

        start, end = 0,0
        if arr[i] == 'S' :
            start, end = (i+j)//2, i
        else :
            start, end = j, (i+j)//2 if (i+j) % 2 == 0 else (i+j)//2 + 1

        for k in range(start, end-1, -1) :
            unique_arr[k] = True

        break

print(sum(unique_arr[a:b+1]))