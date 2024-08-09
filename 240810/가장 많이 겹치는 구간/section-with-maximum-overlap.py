n = int(input())
dotList = list()
for _ in range(n):
    a, b = tuple(map(int, input().split()))
    dotList.append((a, +1))
    dotList.append((b, -1))

dotList.sort()
ans = 0
sumResult = 0
for x, sumNum in dotList:
    sumResult += sumNum
    ans = max(ans, sumResult)

print(ans)