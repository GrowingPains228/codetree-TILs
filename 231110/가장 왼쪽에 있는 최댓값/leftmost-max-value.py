n = int(input())
arr = list(map(int, input().split()))

index = n

while True :
    if index == 0 :
        break
    max_num = -1
    #순회하면서 가장 왼쪽에 있는 최댓값의 위치를 출력
    for i in range(0,index) : 
        if max_num < arr[i] :
            max_num = arr[i]
            index = i
    print(index + 1, end = " ")