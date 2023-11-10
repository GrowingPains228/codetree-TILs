#2행 4열 2차 배열
arr_2d = [list(map(int, input().split())) for _ in range(2)]
#조금 있다가 전체 평균에 더할 놈
new_arr = []

#가로 평균 + 그 값들 넣어주기
for i in arr_2d :
    print(f"{sum(i)/len(i):.1f}", end = " ")
    new_arr.append(sum(i)/len(i))
print()


#세로 평균
for i in range(4) : 
    total = 0
    for j in range(2) : 
        total += arr_2d[j][i]
    print(f"{total/2:.1f}", end = " ")
print()

print(f"{sum(new_arr)/len(new_arr):.1f}")