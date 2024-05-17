import sys

INT_MIN = -sys.maxsize
    
# 변수 선언 및 입력
n = int(input())

# 초기 조건으로 아직 아무런 알바도 진행하지 못했을 경우에 대한
# 상태를 정의합니다. 편의를 위해 후에
# 0번째 index와 비교했을 때 항상 갱신될 수
# 있도록 s[0], e[0], p[0]를 전부 0으로 설정합니다.
s = [
    0
    for _ in range(n + 1)
]
e = [
    0
    for _ in range(n + 1)
]
p = [
    0
    for _ in range(n + 1)
]

sorted_works = list()
    
# dp[i] : 마지막으로 고른 알바가 i번째 알바일 때,
# 얻을 수 있었던 최대 수익
# 최대를 구하는 문제이므로, 초기에는 전부 INT_MIN을 넣어줍니다.
dp = [INT_MIN for _ in range(n + 1)]

# 입력:
for i in range(1, n + 1):
    s[i], e[i], p[i] = tuple(map(int, input().split()))

def preprocess():
    # 알바가 끝나는 날짜 순으로 정렬하여 이후에 dp값을 계산할 때
    # e[j] < s[i]를 만족하는 j의 경우를
    # 중복하여 계산하지 않도록 합니다.
    for i in range(0, n + 1):
        sorted_works.append((e[i], i))
    sorted_works.sort()


# 마지막으로 고른 알바가 0번째 알바일 때
# 지금까지 수익이 0이었다는 뜻으로
# dp[0] = 0을 초기 조건으로 설정합니다.
dp[0] = 0

preprocess()


# 마지막으로 고른 알바가 i번째 알바일 때,
# 얻을 수 있었던 최대 수익을 계산합니다.

# 0부터 i -1 사이의 j중 e[j] < s[i]를 만족하며
# dp[j]값이 가장 큰 경우의 j값을 기록합니다.
# 처음에는 0번째 위치가 유일하게 가능한 위치입니다.
max_j = 0

# i가 증가함에 따라 dp값을 최대로 하는 j를 중복 없이 계산해주기 위해서는
# e[i]가 증가하는 순으로 정렬해놓은 sorted_works 배열을 활용하여
# e[j] < s[i]를 만족하는 알바에 대해 그 중 dp값이 가장 큰 j를 계산하면 됩니다.
ptr = 1

for i in range(1, n + 1):
    # i번째 보다 앞에 있는 알바들 중 (j) i번째와 일하는 기간이
    # 겹치지 않는 알바들에 대해 해당 알바 다음에 i번째 알바를 진행하는 경우를
    # 계산하여 그 중 최대 수익을 dp[i]에 적어줍니다.
    
    # s[i - 1] <= e[j] < s[i]를 만족하는 알바에 대해
    # 추가적으로 dp[j] 값을 더 크게 만들 수 있는지를 확인하여 
    # 가장 큰 값이 되도록 갱신합니다.
    while sorted_works[ptr][0] < s[i]:
        j = sorted_works[ptr][1]
        if dp[j] > dp[max_j]:
            max_j = j
            
        ptr += 1
            
    dp[i] = max(dp[i], dp[max_j] + p[i])
    
# 마지막으로 진행한 알바가 i번째인 경우를
# 전부 조사하여 그 중 수익을 가장 크게 얻을 수 있는 경우를 선택합니다.            
answer = 0
for i in range(0, n + 1):
    answer = max(answer, dp[i])
    
print(answer)