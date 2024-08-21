import sys
n = int(input())
a,b = map(int, input().split())


# 정답 안에 있는지 체크 하기 위한 함수
def InRange(value):
    return a <= value <= b


def binary_search(target):
    global a, b
    left, right = 1, n

    cnt = 0
    while left <= right:
        cnt += 1
        mid = (left + right)//2
        if mid == target:
            return cnt

        if mid >= target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


max_ans = 0
min_ans = sys.maxsize

for elem in range(a, b+1):
    cnt = binary_search(elem)
    min_ans = min(min_ans, cnt)
    max_ans = max(max_ans, cnt)

print(min_ans, max_ans)