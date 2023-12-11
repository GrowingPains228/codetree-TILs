import sys
MAX_INT = sys.maxsize
n = 6
arr = list(map(int, input().split()))
arr.sort()

team1 = arr[0] + arr[5]
team2 = arr[1] + arr[4]
team3 = arr[2] + arr[3]
max_team = max(team1, team2, team3)
min_team = min(team1, team2, team3)

print(max_team - min_team)