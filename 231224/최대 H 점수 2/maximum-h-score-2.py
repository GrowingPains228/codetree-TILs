MAX_VALUE = 100

n,l = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

ans = 0
# H 점수라고 가정하고 
for i in range(MAX_VALUE + 1) :


    possible = True
    cnt = 0
    for j in range(n) :
        if arr[j] < i :
            continue

        cnt += 1
        
    if cnt >= i + 1 :
        ans = max(ans, i+1)

print(ans)