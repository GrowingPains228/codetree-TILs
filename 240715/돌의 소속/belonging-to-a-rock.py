# 주제 : Prefix Sum
# 이름 : 돌의 소속
n, q = map(int, input().split())
group = [[0]*(n+1) for _ in range(4)]


def getSum(s, e, idx):
    return group[idx][e] - group[idx][s-1]


def main():
    for i in range(1, n+1):
        num = int(input())
        if num == 1:
            group[1][i] += 1
        elif num == 2:
            group[2][i] += 1
        else:
            group[3][i] += 1

    for i in range(1, 4):
        for j in range(1, n+1):
            group[i][j] = group[i][j-1] + group[i][j]

    for _ in range(q):
        s,e = map(int, input().split())
        print(getSum(s, e, 1), getSum(s, e, 2), getSum(s, e, 3))


if __name__ == "__main__":
    main()