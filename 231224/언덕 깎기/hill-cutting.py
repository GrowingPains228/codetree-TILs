import sys
MAX_INT = sys.maxsize
MAX_HEIGHT = 100
MAX_RANGE = 1000

n = int(input())
k = 17
arr = [
    int(input()) for _ in range(n)
]

ans = MAX_INT
for i in range(MAX_HEIGHT) :

    cost = 0
    for j in range(n) :
        if arr[j] < i :
            cost += (i - arr[j]) ** 2
        if arr[j] > i + k :
            cost += (arr[j] - i - k) ** 2
    
    ans = min(ans, cost)

print(ans)