n, k = tuple(map(int, input().rstrip().split()))
rotation = list(input())

mapper = {
    'L': 0,
    'R': 1
}

# dp[i][j] : i 번째 수정이 나올때, 지금까지 j번 이동했을 때 얻은 수정의 최대 개수
dp = [[0]*(k+1) for _ in range(n)]
# 한번도 안 바꿀 경우는 초기화로 값 넣어주기
dp[0][0] = 1 if rotation[0] == 'L' else 0
for i in range(1, n):
    if rotation[i] == 'L':
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]

for i in range(1, n):
    for j in range(1, k+1):
        if j % 2 != mapper[rotation[i]]:
            continue

        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1

print(max(dp[n-1]))