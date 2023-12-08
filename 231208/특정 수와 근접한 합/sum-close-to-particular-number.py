import sys
INT_MAX = sys.maxsize

n,s = tuple(map(int, input().split()))

#S 와 최대한 가까워 지는건 S와 빼서 0에 가장 가까운 경우
arr = list(map(int, input().split()))

def return_sum(idx1, idx2) :
    value = 0
    for i in range(n) :
        if i == idx1 or i == idx2 :
            continue
        value += arr[i]
    return value

ans = INT_MAX
for i in range(n) :
    for j in range(i+1, n) :
        sum_value = return_sum(i,j)

        ans = min(ans, abs(s-sum_value))

print(ans)