N, T = map(int, input().split())
arr = [int(input()) for _ in range(N)]


def Is_Possible(max_cnt):
    global N, T
    timeList = [0] * (T+1)
    cnt = 0
    idx = 0
    for i in range(T+1):
        if timeList[i] != 0:
            cnt -= timeList[i]
            timeList[i] = 0

        while cnt < max_cnt and idx < N:
            if i + arr[idx] > T:
                return False

            timeList[i + arr[idx]] += 1
            idx += 1
            cnt += 1

    return idx == N and cnt == 0

# 시간 복잡도 : TlogN
left, right = 1, N
ans = N
while left <= right:
    mid = (left + right)//2
    if Is_Possible(mid):
        ans = min(ans, mid)
        right = mid - 1
    else:
        left = mid + 1
print(ans)