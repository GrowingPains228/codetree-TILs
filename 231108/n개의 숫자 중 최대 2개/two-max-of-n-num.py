n = int(input())
arr = list(map(int, input().split()))

# 리스트의 처음 요소와 그다음 요소를 비교
# 더 작은 쪽은 오른쪽으로, 저 큰쪽은 왼쪽으로 돌려준다
for i in range(n-1) :
    for j in range(1,n-i) :
        if arr[j-1] <= arr[j] :
            arr[j-1], arr[j] = arr[j], arr[j-1]

print(arr[0], arr[1])