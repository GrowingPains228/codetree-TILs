n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
countingDict = dict()
length = len(arr)
j = 0
ans = 0
for i in range(1, length):
    while j + 1 < length :
        if arr[j+1] not in countingDict or countingDict.get(arr[j+1], 0) + 1 <= k:
            countingDict[arr[j+1]] = countingDict.get(arr[j+1], 0) + 1
            j += 1
        else:
            break

    ans = max(ans, j - i + 1)
    countingDict[arr[i]] -= 1
print(ans)