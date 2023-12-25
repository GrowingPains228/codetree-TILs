n = int(input())
before = [0] + list(map(int, input().split()))
after = [0] + list(map(int, input().split()))

ans = 0

for i in range(1, n+1) :
    if before[i] > after[i] :
        cnt = before[i] - after[i]
        before[i+1] += cnt
        before[i] -= cnt
        ans += cnt

print(ans)