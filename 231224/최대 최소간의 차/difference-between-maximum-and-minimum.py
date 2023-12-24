import sys
MAX_INT = sys.maxsize
MAX_VALUE = 10000
n,k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

ans = MAX_INT
# 가장의 값의 범위를 설정하여 로직을 구현한다.
for i in range(MAX_VALUE - k + 1) :
    cost = 0
    for j in range(n):
        if arr[j] >= i and arr[j] <= i + k :
            continue
        
        cost += (i - arr[j]) if arr[j] < i else (arr[j] - (i+k))
    
    ans = min(ans, cost)

print(ans)