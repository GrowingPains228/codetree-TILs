import sys

n = int(input())
arr = list(map(int, input().split()))

ans = sys.maxsize
for i in range(n) :
    temp_moving = 0
    for  j in range(n) :
        if j == i :
            continue

        distance = abs(i - j)
        people = arr[j]
        temp_moving += distance * people
        
    ans = min(temp_moving, ans)

print(ans)