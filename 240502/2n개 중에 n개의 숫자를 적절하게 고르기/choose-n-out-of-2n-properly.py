import sys

n = int(input())
arr = list(map(int, input().split()))
ans = sys.maxsize


def find_min(idx, cnt, diff):
    global ans

    if idx == 2*n:
        if cnt == n:
            ans = min(ans, abs(diff))
        return

    find_min(idx+1, cnt+1, diff + arr[idx])
    find_min(idx+1, cnt, diff-arr[idx])


find_min(0, 0, 0)
print(ans)