from collections import defaultdict
string = [' '] + list(input())
length = len(string)
countingDict = defaultdict(int)

j = 0
ans = 0
for i in range(1, length):
    while j + 1 < length :
        if string[j+1] not in countingDict or countingDict[string[j+1]] == 0:
            countingDict[string[j + 1]] += 1
            j += 1
        else:
            break

    ans = max(ans, j - i + 1)

    countingDict[string[i]] -= 1

print(ans)