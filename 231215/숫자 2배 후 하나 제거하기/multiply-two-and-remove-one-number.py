import sys
INT_MAX = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

ans = INT_MAX
for i in range(n):
    arr[i] *= 2


    for j in range(n) :
        remaining_arr = [elem for (k,elem) in enumerate(arr) if j != k]

        result = 0
        for z in range(n-2) :
            result += abs(remaining_arr[z+1] - remaining_arr[z])
        
        ans = min(ans, result)
        
    arr[i] //= 2

print(ans)