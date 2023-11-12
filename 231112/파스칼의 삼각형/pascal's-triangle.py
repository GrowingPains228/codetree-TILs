n = int(input())

arr_triangle = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 1열 초기화
for i in range(n) :
    arr_triangle[i][0] = 1


for i in range(1, n) :
    for j in range(1, i+1) :
        arr_triangle[i][j] = arr_triangle[i-1][j-1] + arr_triangle[i-1][j]

for i in range(n) :
    for j in range(i+1) : 
        print(arr_triangle[i][j], end = " ")
    print()