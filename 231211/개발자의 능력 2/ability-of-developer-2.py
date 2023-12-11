import sys
MAX_INT = sys.maxsize
n = 6
arr = list(map(int, input().split()))

def diff(i, j, k, m) :
    team1 = arr[i] + arr[j]
    team2 = arr[k] + arr[m]
    team3 = sum(arr) - team1 - team2

    # 세팀의 차이 중 최대값을 리턴함. => 그래야 팀 스코어가 가장 큰 팀과 가장 작은 팀의 차이가 최소가 되도록 할 수 있음.
    ret = abs(team1 - team2)
    ret = max(ret, abs(team1 - team3))
    ret = max(ret, abs(team2 - team3))

    return ret

min_diff = MAX_INT
for i in range(n) :
    for j in range(i + 1, n) :
        for k in range(n) :
            for m in range(k + 1, n) :
                if i == k or i == m or j == k or j == m :
                    continue
                min_diff = min(min_diff, diff(i, j, k, m))

print(min_diff)