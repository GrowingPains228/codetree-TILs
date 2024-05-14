import sys

INT_MAX = sys.maxsize
MAX_R = 100

# 입력 받기
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [0]*n
    for _ in range(n)
]

ans = INT_MAX


def initailize() :
    for i in range(n):
        for j in range(n):
            dp[i][j] = INT_MAX
    
    # 시작점의 경우, grid 시작점으로 초기화
    dp[0][0] = grid[0][0]

    # 최좌측 열 및 행의 초기값을 설정
    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1], grid[0][i])
        dp[i][0] = max(dp[i-1][0], grid[i][0])


def solve(lower_bound):
    #lower_bound 미만의 값은 사용할 수 없도록
    #grid 값을 번경해준다.
    for i in range(n):
        for j in range(n):
            if grid[i][j] < lower_bound:
                grid[i][j] = INT_MAX
    
    # DP 초기화
    initailize()

    # 탐색하는 위치의 위에 값과 좌측 값 중에 작은 값과
    # 해당 위치의 숫자 중에 최댓값을 구해준다.
    for i in range(1,n):
        for j in range(1,n):
            dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), grid[i][j])
    
    return dp[n-1][n-1]


# 최솟값을 k라고 가정했을 때
# lower_bound 이상의 수들만 사용하여
# 이동한다는 조건하에서
# 최댓값을 최소로 만드는 DP문제를 풀어준다.
for lower_bound in range(1, MAX_R+1):
    upper_bound = solve(lower_bound)

    if upper_bound == INT_MAX:
        continue
    
    ans = min(ans, upper_bound - lower_bound)

print(ans)