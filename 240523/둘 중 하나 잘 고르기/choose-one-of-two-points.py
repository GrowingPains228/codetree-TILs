n = int(input())
cards = [(0,0)] + [
    tuple(map(int, input().split()))
    for _ in range(2*n)
]

# 파란카드 n개, 빨간카드 n개를 뽑는다고 했을때,
# 마지막에 파란카드를 뽑을때, 이전까지 파란카드 n-1개, 빨간카드 n개를 뽑기까지 가장 큰 합을 구하고 있었을 것이고
# 마지막에 빨간 카드를 뽑을때, 역시 파란카드 n개, 빨간카드 n-1개를 뽑아 놓을 것이다.
# dp[i][j]를 정의해보면, i는 현재 시퀀스, j는 뽑은 빨간카드의 갯수이다.
dp = [[-1]*(n+1) for _ in range(2*n+1)]
dp[0][0] = 0
red1, blue1 = cards[1]
dp[1][0] = blue1
dp[1][1] = red1

for i in range(2, 2*n+1):
    red, blue = cards[i]
    for j in range(n+1):
        if i < j:
            continue

        # 빨간색 카드를 선택 안하는 경우
        dp[i][j] = max(dp[i][j], dp[i-1][j] + blue)

        # 빨간색 카드를 선택 하는 경우
        dp[i][j] = max(dp[i][j], dp[i-1][j-1] + red)

print(dp[2*n][n])