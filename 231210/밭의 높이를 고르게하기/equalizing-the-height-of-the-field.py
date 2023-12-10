import sys
MAX_NUM = sys.maxsize

n,h,t = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

cal = MAX_NUM
for i in range(n) :
    if i + t <= n :
        cnt = 0
        for j in range(i, i+t) :
            if arr[j] == h :
                continue
            
            cnt += abs(h - arr[j])
        cal = min(cal, cnt)

print(cal)