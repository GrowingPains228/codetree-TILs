import sys
INT_MIN = -sys.maxsize

#변수 입력 및 선언
n = int(input())

s = [0]* (n+1)
e = [0]* (n+1)
p = [0]* (n+1)

sorted_works = list()

dp = [INT_MIN]*(n+1)

for i in range(1,n+1):
    s[i], e[i], p[i] = tuple(map(int, input().split()))


def preprocess():
    for i in range(n+1):
        sorted_works.append((e[i], i))
    sorted_works.sort()


dp[0] = 0
preprocess()

max_j = 0
ptr = 1

for i in range(1, n+1):
    while sorted_works[ptr][0] < s[i]:
        j = sorted_works[ptr][1]
        if dp[j] > dp[max_j]:
            max_j = j
        
        ptr += 1

    dp[i] = max(dp[i], dp[max_j] + p[i])
    print(dp[i])


print(max(dp))