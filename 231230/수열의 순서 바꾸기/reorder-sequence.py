n = int(input())
arr = list(map(int, input().split()))

# 1. 오름차순이 맞지 않는 큰 숫자가 중간에 있으면, 제일 앞에서부터 큰 숫자까지 뒤로 이동해야한다.
idx = 0
for i in range(n-1) :
    if arr[i] > arr[i+1] :
        idx = i


print(idx+1)