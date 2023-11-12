n = int(input())
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num = 1

for i in range(n) : 
    for j in range(n) :
        arr_2d[j][i] = num
        num += 1

for row in arr_2d :
    for elem in row : 
        print(elem, end = " ")
    print()