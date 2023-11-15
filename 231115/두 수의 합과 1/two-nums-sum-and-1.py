a,b = tuple(map(int, input().split()))
sum_string = str(a+b)

cnt = 0

for elem in sum_string :
    if elem == '1' :
        cnt += 1
    
print(cnt)