import sys
n, m = map(int, input().split())
fireList = list(map(int, input().split()))
fireList.sort()
fireFighterList = list(map(int, input().split()))
fireFighterList.sort()

j = 0   # 소방서 인덱스
ans = 0
for i in range(n):
    while j+1 < m and abs(fireList[i] - fireFighterList[j]) >= abs(fireList[i] - fireFighterList[j+1]):
        j += 1

    ans = max(ans, abs(fireList[i] - fireFighterList[j]))

print(ans)