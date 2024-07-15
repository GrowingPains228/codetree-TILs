import sys
MAX_SIZE = sys.maxsize


def prefixSum(a, b, group):
    return group[a] - group[b]


# 입력 받고
if __name__ == "__main__":
    n, k, b = map(int, input().split())
    removeArr = [True] * (n + 1)
    removeCntSum = [0] * (n + 1)

    for _ in range(b):
        idx = int(input())
        removeArr[idx] = False

    for i in range(1, n + 1):
        removeCntSum[i] = removeCntSum[i - 1] + (0 if removeArr[i] else 1)

    ans = MAX_SIZE
    for i in range(k, n + 1):
        ans = min(ans, prefixSum(i, i - k, removeCntSum))

    print(ans)