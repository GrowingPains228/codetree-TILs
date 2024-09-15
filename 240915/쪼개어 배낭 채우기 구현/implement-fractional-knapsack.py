n, m = map(int, input().split())
jewels = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
ans = 0

# 가치/ 무게가 내림차순이 되도록 정렬
jewels.sort(key=lambda x: -x[1]/x[0])

for w, v in jewels:
    if m >= w:
        m -= w
        ans += v
    else:
        ans += m * v/w
        break

print(f"{ans:.3f}")