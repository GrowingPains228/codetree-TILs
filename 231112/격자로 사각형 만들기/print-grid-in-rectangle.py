n = int(input())

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n) :
    arr_2d[i][0] = 1
    arr_2d[0][i] = 1


for i in range(1,n) :
    for j in range(1,n) :
        arr_2d[i][j] = arr_2d[i-1][j-1] + arr_2d[i][j-1] + arr_2d[i-1][j]

for row in arr_2d :
    for elem in row :
        print(elem, end = " ")
    print()