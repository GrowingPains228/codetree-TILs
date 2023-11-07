n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n) :
    if arr[i] == 2 and cnt == 2 :
        print(i+1)
    else :
        cnt += 1