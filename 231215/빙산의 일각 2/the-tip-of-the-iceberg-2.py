n = int(input())
arr = [
    int(input()) for _ in range(n)
]

# True 이면 현재 빙산의 개수를 센것이다.

ans = 0
for i in range(n) :
    ground = arr[::]

    for k in range(n) :
        ground[k] -= arr[i]

    is_ice = False
    cnt = 0
    for j in range(n) :
        if ground[j] <= 0 :
            is_ice = False

        elif ground[j] > 0 :
            if is_ice :
                continue

            is_ice = True
            cnt += 1
    ans = max(ans, cnt)
    
print(ans)