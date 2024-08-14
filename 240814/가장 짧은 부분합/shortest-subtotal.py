import sys
n, s = map(int, input().split())
arr = [0] + list(map(int, input().split()))

ans = sys.maxsize
sum_val = 0
j = 0
for i in range(1, n):
    while j + 1 < n and sum_val + arr[j+1] < s:
        sum_val += arr[j+1]
        j += 1

    ans = min(ans, j + 2 - i)
        
    sum_val -= arr[i]

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)