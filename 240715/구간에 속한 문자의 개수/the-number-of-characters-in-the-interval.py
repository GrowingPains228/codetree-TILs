def getSum(r1, c1, r2, c2, board):
    return board[r2][c2] - board[r1-1][c2] - board[r2][c1-1] + board[r1-1][c1-1]


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    board = [[''] * (m+1)] + [([''] + list(input()))for _ in range(n)]
    cnt_a = [[0] * (m+1) for _ in range(n+1)]
    cnt_b = [[0] * (m+1) for _ in range(n+1)]
    cnt_c = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            cnt_a[i][j] = cnt_a[i - 1][j] + cnt_a[i][j - 1] - cnt_a[i - 1][j - 1]
            cnt_b[i][j] = cnt_b[i - 1][j] + cnt_b[i][j - 1] - cnt_b[i - 1][j - 1]
            cnt_c[i][j] = cnt_c[i - 1][j] + cnt_c[i][j - 1] - cnt_c[i - 1][j - 1]

            if board[i][j] == "a":
                cnt_a[i][j] += 1
            elif board[i][j] == "b":
                cnt_b[i][j] += 1
            else:
                cnt_c[i][j] += 1

    for _ in range(k):
        r1, c1, r2, c2 = map(int, input().split())
        print(getSum(r1, c1, r2, c2, cnt_a), getSum(r1, c1, r2, c2, cnt_b), getSum(r1, c1, r2, c2, cnt_c))