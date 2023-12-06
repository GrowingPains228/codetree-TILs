r,c = tuple(map(int, input().split()))
arr = [
    input().split() 
    for _ in range(r)
]

# 각 위치에서 이동할 수 있는 깊이를 나타냄.
count_arr = [
    [0]*c
    for _ in range(r) 
]

cnt = 0
for i in range(1, r-2) :
    for j in range(1, c-2) :
        if arr[0][0] != arr[i][j] :
            for k in range(i + 1, r-1) :
                for z in range(j + 1, c-1) :
                    if arr[i][j] != arr[k][z] and arr[k][z] == arr[i][j]:
                        cnt += 1
print(cnt)