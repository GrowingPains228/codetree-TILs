import sys
n, s = map(int, input().split())
arr = [0] + list(map(int, input().split()))

ans = sys.maxsize
sum_val = arr[1]
j = 1
for i in range(1, n):
    while j + 1 < n :
        if sum_val >= s:
            break;
        sum_val += arr[j+1]
        j += 1
        
    ans = min(ans, j - i + 1)
        
    sum_val -= arr[i]

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)