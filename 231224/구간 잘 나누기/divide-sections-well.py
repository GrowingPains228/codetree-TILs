import sys
MAX_INT = sys.maxsize
MAX_RANGE = 10000


n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
Start_value = max(arr)
ans = MAX_INT
# 최댓값이 누가 되는지 계산하는 로직을 구현한다.
# 배열에서 가장 큰 값이 최댓값이 되므로, 그 지점에서 시작해도 된다.
for i in range(Start_value, MAX_RANGE + 1) :
    #최댓값이 i 라고 가정하고, 구간 짜기
    possible = True
    section = 1

    cnt = 0
    for j in range(n) :
        if arr[j] > i :
            possible = False
            break
        
        # j 번째 숫자를 넣었을때 i 보다 커지면
        # j 번째 숫자부터 다음 구간으로 만든다.
        if cnt + arr[j] > i :
            cnt = 0
            section += 1

        #이번 구간에 j번째 숫자를 집어 넣는다.
        cnt += arr[j]

    if possible and section <= m :
        ans = min(ans, i)

print(ans)