MAX_WEIGHT = 10000

n, m = tuple(map(int, input().split()))

jewelrys = list()
for _ in range(n):
    (weight, value) = tuple(map(int, input().split()))
    jewelrys.append((weight, value))
jewelrys.sort()

dp_weight = [False]*(MAX_WEIGHT+1)
dp_value = [-1]*(MAX_WEIGHT+1)

dp_weight[0] = True
dp_value[0] = 0

for weight, value in jewelrys:
    for j in range(MAX_WEIGHT, -1, -1):
        if weight > j:
            continue
        
        if dp_weight[j - weight] == False:
            continue
        
        dp_weight[j] = True
        dp_value[j] = max(dp_value[j], dp_value[j - weight] + value)


ans = 0
for i in range(1, m+1):
    if dp_weight[i]:
        ans = max(ans, dp_value[i])

print(ans)