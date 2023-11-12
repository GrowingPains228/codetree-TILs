#입력 받기
n = int(input())

# 초기화
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

row_rule = True
cnt = 1
for i in range(n-1, -1, -1) :
    if row_rule :
        for j in range(n-1, -1, -1) : 
            arr_2d[j][i] = cnt
            cnt+=1
            row_rule = False
    else :
        for j in range(n) :
            arr_2d[j][i] = cnt
            cnt+=1
            row_rule = True

for row in arr_2d :
    for elem in row :
        print(elem , end = " ")
    print()