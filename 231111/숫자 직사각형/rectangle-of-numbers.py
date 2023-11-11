n,m = tuple(map(int, input().split()))

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

num = 1
for row in arr_2d :
    for elem in row :
        elem = num
        print(elem, end = " ")
        num += 1
    print()