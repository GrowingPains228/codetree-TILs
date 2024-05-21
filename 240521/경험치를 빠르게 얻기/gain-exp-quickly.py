import sys
MAX_T = 10001
INT_MIN = -sys.maxsize
n,m = tuple(map(int, input().split()))
quest_list = list()
for _ in range(n):
    exp, time = tuple(map(int, input().split()))
    quest_list.append((exp, time))

# index = 시간, value = 경험치
dp = [INT_MIN]* (MAX_T+1)
dp[0] = 0

for exp, time in quest_list:
    for j in range(MAX_T, -1, -1):
        if j >= time and dp[j - time] != INT_MIN:
            dp[j] = max(dp[j], dp[j-time] + exp)

ans_t = 0
for i in range(1, MAX_T+1):
    if dp[i] >= m:
        ans_t = i
        break

print(ans_t)