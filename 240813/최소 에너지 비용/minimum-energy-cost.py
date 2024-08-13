n = int(input())
movableCost = list(map(int, input().split())) # 각 장소마다 이동하는데 필요한 에너지 비용
FillPoint = list(map(int, input().split())) # 장소(n)별 1에너지를 충전하는데 드는 에너지 비용

# 왼쪽에서부터 가장 적은 비용이 드는 곳을 업데이트 한다.
minR = [0] * n
minR[0] = FillPoint[0]
for i in range(1, n):
    minR[i] = min(minR[i-1], FillPoint[i])

ans = 0
for i in range(n-1):
    ans += minR[i] * movableCost[i]

print(ans)