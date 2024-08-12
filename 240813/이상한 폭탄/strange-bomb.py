n, k = map(int, input().split())

ans = 0
bombList = dict()
for i in range(n):
    num = int(input())
    if num in bombList and abs(i - bombList[num]) <= k:
        ans = max(ans, num)
    
    bombList[num] = i

print(ans)