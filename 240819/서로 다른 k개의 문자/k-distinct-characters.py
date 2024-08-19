string, k = input().split()
k = int(k)
wordDict = dict()
string = ['#'] + list(string)
length = len(string)

j = 0
distinct_number = 0
ans = 0
for i in range(1, length):
    while j + 1 < length:
        if wordDict.get(string[j + 1], 0) != 0 or distinct_number + 1 <= k:
            wordDict[string[j + 1]] = wordDict.get(string[j + 1], 0) + 1
            if wordDict[string[j + 1]] == 1:
                distinct_number += 1
            j += 1
        else:
            break

    ans = max(ans, j - i + 1)

    wordDict[string[i]] -= 1
    if wordDict[string[i]] == 0:
        distinct_number -= 1

print(ans)