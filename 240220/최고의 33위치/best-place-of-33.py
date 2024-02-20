ans_length = 3
n = int(input())

arr = [
    list(map(int, input().split())) for _ in range(n)
]

ans = 0
for i in range(n) :
    if i + ans_length -1 >= n  :
        continue

    for j in range(n) :
        if j + ans_length -1 >= n  :
            continue
        
        # 총합 구하기
        cnt = 0
        for a in range(ans_length) :
            for b in range(ans_length) :
                cnt += arr[i + a][j + b]
        ans = max(ans, cnt)

print(ans)