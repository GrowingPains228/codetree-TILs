MAX_SIZE = 1000
n = int(input())
memo = [-1] * (MAX_SIZE+1)


def climb_memoization(n):
    if n <= 1:
        return 0

    if memo[n] != -1:
        return memo[n]

    if n == 2 or n == 3:
        return 1

    memo[n] = climb_memoization(n-2) + climb_memoization(n-3)
    return memo[n]


print(climb_memoization(n)%10007)