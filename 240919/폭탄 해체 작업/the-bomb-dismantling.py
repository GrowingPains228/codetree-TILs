# 시간대 별로 가장 점수가 높은 순서대로 폭탄을 해제한다.
n = int(input())

timeList = []
for _ in range(n):
    timeList.append(tuple(map(int, input().split())))

timeList.sort(key = lambda x : (x[1], -x[0]))

curTime = 0
ans = 0
for value, time in timeList:
    if curTime < time:
        curTime += 1
        ans += value

print(ans)