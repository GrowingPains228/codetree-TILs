MAX_SIZE = 19
n = int(input())

dp = [0]* (MAX_SIZE + 1)
dp[0] = 1
dp[1] = 1


def get_num_of_unique_bst(n):
    ans_num = 0

    for i in range(n):
        ans_num += dp[i]*dp[n-i-1]
    
    return ans_num


for i in range(2, n+1):
    dp[i] = get_num_of_unique_bst(i)

print(dp[n])