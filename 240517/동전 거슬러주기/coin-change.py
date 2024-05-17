import sys
sys.setrecursionlimit(10000)

INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))

coin = [0] + list(map(int, input().split()))

ans = INT_MAX

def find_min_cnt(sum, cnt):
    global ans

    if sum == m:
        ans = min(ans, cnt)
        return
    
    for i in range(1, n+1):
        if sum + coin[i] <= m:
            find_min_cnt(sum + coin[i], cnt+1)


find_min_cnt(0,0)

if ans == INT_MAX:
    print(-1)
else:
    print(ans)