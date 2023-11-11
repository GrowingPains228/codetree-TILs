n,m = tuple(map(int, input().split()))

arr_2d_1 = [
    list(map(int, input().split()))
    for _ in range(n)
]

arr_2d_2 = [
    list(map(int, input().split()))
    for _ in range(n)
]

new_Arr_2d = [ [1 for _ in range(m)] for _ in range(n)]

for i in range(n) :
    for j in range(m) :
        if arr_2d_1[i][j] == arr_2d_2[i][j] :
            new_Arr_2d[i][j] = 0
        
for row in new_Arr_2d :
    for elem in row :
        print(elem, end = " ")
    print()