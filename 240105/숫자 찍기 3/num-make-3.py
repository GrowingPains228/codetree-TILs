n,m = tuple(map(int, input().split()))
arr = [ [0]*n for _ in range(n) ]

#일단 파스칼 삼각형으로 구하고 값 세팅하기
arr[0][0] = 1
for i in range(1,n) :
    for j in range(n) :
        v1 = 0 if j -1 < 0 else arr[i-1][j-1]
        v2 = arr[i-1][j]
        
        arr[i][j] =  v1 + v2


if m == 1 :
    for i in range(n) :
        for j in range(i+1) :
            print(arr[i][j], end = " ")
        print()
elif m == 2:
    for i in range(n-1, -1, -1) :
        print(' '*(n-i-1), end = "")
        for j in range(n) :
            if arr[i][j] == 0 :
                break

            print(arr[i][j], end = " ")
        print()
else  :
    for i in range(n-1, -1, -1) :
        for j in range(n -1, -1, -1) :
            if arr[j][i] == 0 :
                break

            print(arr[j][i], end = " ")
        print()