n = int(input())
valueList = list(map(int, input().split()))

ans = 0
min_value = valueList[0]
for i in range(1, n):
    if valueList[i] > min_value:
        ans = max(ans, valueList[i] - min_value)
    else:
        min_value = valueList[i]

print(ans)