n = int(input())

nums = []
numCountDic = dict()

# 가능한 가능 작은 최댓값을 만들려고 하면
# 제일 큰 수는 제일 작은 수랑 매치해주면 된다.
for i in range(n):
    cnt, number = map(int, input().split())
    numCountDic[number] = cnt
    nums.append(number)

nums.sort()

startIdx = 0
endIdx = n-1
ans = 0

while startIdx <= endIdx:
    num1, num2 = nums[startIdx], nums[endIdx]
    ans = max(ans, num1 + num2)
    
    numCountDic[num1] -= 1
    numCountDic[num2] -= 1

    if numCountDic[num1] == 0:
        startIdx += 1
    
    if numCountDic[num2] == 0:
        endIdx -= 1

print(ans)