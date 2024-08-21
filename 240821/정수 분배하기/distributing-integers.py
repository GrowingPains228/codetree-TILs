n, m = tuple(map(int, input().split()))

arr = list()
total = 0
for _ in range(n):
    num = int(input())
    arr.append(num)
    total += num


def is_possible(max_num):
    global m
    result_cnt = 0
    for elem in arr:
        result_cnt += elem // max_num

    return result_cnt >= m


ans = 0
left, right = 1, total//m
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)