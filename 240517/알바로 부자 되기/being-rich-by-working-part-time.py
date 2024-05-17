n = int(input())
work_list = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
dp = [0]*n
_, _, p = work_list[0]
dp[0] = p

# 최장 증가 수열을 만들면서
# 총 돈을 업데이트 해야함.
for i in range(1,n):
    s1, e1, p1 = work_list[i]
    dp[i] = p1
    for j in range(i):
        s2, e2, p2 = work_list[j]

        if e2 >= s1:
            continue
        
        dp[i] = max(dp[i], dp[j] + p1)

print(max(dp))