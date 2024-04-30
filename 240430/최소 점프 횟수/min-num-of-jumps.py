n = int(input())
jump_arr = list(map(int, input().split()))
ans = -1

def recursion_Jump(idx, cnt):
    global ans
    if idx == n-1: # 끝 지점에 도착 했으면
        ans = cnt if ans == -1 else min(ans, cnt)
        return

    # 끝에 도착 안했는데, 발판이 0이면 도달 못하는 것.
    if jump_arr[idx] == 0:
        return

    for i in range(1, jump_arr[idx]+1):
         recursion_Jump(idx+i, cnt + 1)


recursion_Jump(0, 0)
print(ans)