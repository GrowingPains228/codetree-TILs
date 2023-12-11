import sys
MAX_INT = sys.maxsize
n = 5
arr = tuple(map(int, input().split()))

def diff(i, j, k) :
    team1 = arr[i] + arr[j]
    team2 = arr[k]
    team3 = sum(arr) - team1 - team2

    if team1 == team2 or team2 == team3 or team1 == team3 :
        return 0

    ref = abs(team1- team2)
    ref = max(ref, abs(team1 - team3))
    ref = max(ref, abs(team2 - team3))

    return ref

min_score = MAX_INT
for i in range(n) :
    for j in range(i + 1, n) :
        for k in range(n) :
            if i == k or j == k :
                continue

            if diff(i, j, k) != 0:
                min_score = min(min_score, diff(i, j, k))

print(min_score if min_score != MAX_INT else -1)