import sys

INT_MIN = -sys.maxsize
MAX_VALUE = 10000

n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [[0] * m for _ in range(n)]


def initialize():
    for i in range(m):
        for j in range(n):
            dp[i][j] = 0

    dp[0][0] = 1


initialize()
for i in range(1, n):
    for j in range(1, m):

        for lx in range(i):
            for ly in range(j):

                if dp[lx][ly] == 0 or grid[lx][ly] >= grid[i][j]:
                    continue

                dp[i][j] = max(dp[i][j], dp[lx][ly] + 1)

print(max([max(row) for row in dp]))