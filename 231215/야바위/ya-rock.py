n = int(input())

arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

cups = [False] * 3
ans = 0
for i in range(3) :
    tmp_cups = cups[::]
    tmp_cups[i] = True

    cnt = 0
    for (a,b,c) in arr :
        tmp_cups[a-1], tmp_cups[b-1] = tmp_cups[b-1], tmp_cups[a-1]
        if tmp_cups[c-1] :
            cnt += 1
    ans = max(ans, cnt)

print(ans)