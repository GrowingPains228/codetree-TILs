n = int(input())
arr = list(map(int, input().split()))
arr.sort()

# 오름차순으로 받은 리스트
arr1 = arr[:n]

# 내림차순으로 받은 리스트
arr2 = arr[2*n-1:n-1:-1]

max_group = 0

for a,b in zip(arr1, arr2) :
    if max_group < (a + b) :
        max_group = a + b
    
print(max_group)