n = int(input())
memo = [-1] * (n+1)
dp = [0] * (n+1)
dp[1], dp[2] = 1,1


def Fibbo_Memoization(n):
    if memo[n] != -1:
        return memo[n]

    if n <= 2:
        return 1
    else :
        memo[n] = Fibbo_Memoization(n-1) + Fibbo_Memoization(n-2)

    return memo[n]


def Fibbo_Tabulation(n):
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


#print(f"Fibbo by Memoization : {Fibbo_Memoization(n)}")
#print(f"Fibbo by Tabulation : {Fibbo_Tabulation(n)}")
Fibbo_Tabulation(n)
print(dp[n])