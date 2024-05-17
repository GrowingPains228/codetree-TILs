import sys
INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))
coin = [0] + list(map(int, input().split()))

memo = [INT_MAX] * (m+1)

def find_min_cnt(sum):
    if memo[sum] != INT_MAX:
        return memo[sum]
    
    # 합이 m이 되면 동전이 추가적으로 필요 없으므로
    # 필요한 동전의 수 0을 반환한다.
    if sum == m:
        memo[sum] = 0
        return 0

    ans = INT_MAX
    for i in range(1, n+1):
        if sum + coin[i] <= m:
            ans = min(ans, find_min_cnt(sum + coin[i]) + 1)
        
    memo[sum] = ans
    return ans


ans_sum = find_min_cnt(0)

if ans_sum == INT_MAX:
    print(-1)
else:
    print(ans_sum)