import sys
n = int(input())
nums = list(map(int, input().split()))

ans = -sys.maxsize
cur_Sum = 0
for i in range(n):  
    if cur_Sum + nums[i] < 0:
        cur_Sum = nums[i]
    else:
        cur_Sum += nums[i]
    ans = max(ans, cur_Sum)

print(ans)