n, k = map(int, input().split())


def InRange(x,y):
    return 1 <= x <= n and 1 <= y <= n


def getSum(x, y, board):
    result = 0
    for r in range(-k, k+1):
        ny = y+r
        if ny < 0 or ny > n:
            continue

        result += board[ny][min(x+(k-abs(r)), n)] - board[ny][max(x-(k-abs(r))-1, 0)]
    return result


if __name__ == "__main__":
    board = [[0]*(n+1)] + [([0] + list(map(int, input().split()))) for _ in range(n)]
    sumBoard = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            sumBoard[i][j] = sumBoard[i][j-1] + board[i][j]

    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            ans = max(ans, getSum(i, j, sumBoard))

    print(ans)