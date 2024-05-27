n, m = tuple(map(int, input().split()))

clothes = list()
for _ in range(n):
    s, e, v = tuple(map(int, input().split()))
    clothes.append((s, e, v))

# dp[i][j] : i번째 날에 j번째 옷을 마지막으로 선택했을때의 만족도
dp = [[0]*(n+1) for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(n):
        s1, e1, v1 = clothes[j]
        if i < s1 or i > e1 :
            continue

        for k in range(n):
            s2, e2, v2 = clothes[k]
            if i-1 < s2 or i-1 > e2:
                continue

            dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(v1 - v2))

print(max(dp[m]))